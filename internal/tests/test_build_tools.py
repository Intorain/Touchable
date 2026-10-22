"""Check that a new game build cannot reuse removed generated resources."""
import json
from pathlib import Path
import plistlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from build_shaders import check_metallib, metallib_target
from prepare_ios import (shell_controller_haptics, shell_localizations,
                         shell_tv_mode_audio_route, stage_module_tables, stage_shaders)
from workspace import ROOT, WorkspaceError


class GeneratedResourceTests(unittest.TestCase):
    def test_rhythm_heaven_declares_its_supported_languages(self):
        data = json.loads((ROOT / 'games/rhythm-heaven/game.json').read_text())
        self.assertEqual(shell_localizations(data['ios']), [
            'en', 'en-GB', 'fr', 'fr-CA', 'es', 'es-419', 'de', 'it',
            'nl', 'ja', 'ko', 'zh-Hans', 'zh-Hant',
        ])
        with self.assertRaises(WorkspaceError):
            shell_localizations({'localizations': []})
        with self.assertRaises(WorkspaceError):
            shell_localizations({'localizations': ['en', '']})

    def test_ipad_shell_uses_full_screen_landscape(self):
        with (ROOT / 'platform/ios/Info.plist').open('rb') as stream:
            info = plistlib.load(stream)
        self.assertEqual(info['UISupportedInterfaceOrientations~ipad'],
                         ['UIInterfaceOrientationLandscapeLeft', 'UIInterfaceOrientationLandscapeRight'])
        self.assertTrue(info['UIRequiresFullScreen'])

    def test_shell_is_a_game_with_game_mode_and_promotion(self):
        with (ROOT / 'platform/ios/Info.plist').open('rb') as stream:
            info = plistlib.load(stream)
        self.assertEqual(info['LSApplicationCategoryType'], 'public.app-category.games')
        self.assertIs(info['LSSupportsGameMode'], True)
        self.assertIs(info['CADisableMinimumFrameDurationOnPhone'], True)

    def test_controller_haptics_is_an_optional_boolean(self):
        data = json.loads((ROOT / 'games/rhythm-heaven/game.json').read_text())
        self.assertTrue(shell_controller_haptics(data['ios']))
        self.assertFalse(shell_controller_haptics({}))
        with self.assertRaises(WorkspaceError):
            shell_controller_haptics({'controller_haptics': 'yes'})


def metallib_header(platform, major, minor):
    # Header layout of xcrun metallib output: magic, target, file version, type, platform, OS version.
    return b'MTLB' + bytes([1, 0, 2, 0, 9, 0, 0, 0x80 | platform]) + bytes([major, 0, minor, 0]) + bytes(16)


class MetalLibraryTargetTests(unittest.TestCase):
    def test_header_gives_platform_and_minimum_os(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'a.metallib'
            path.write_bytes(metallib_header(2, 27, 1))
            self.assertEqual(metallib_target(path), ('iphoneos', (27, 1)))
            path.write_bytes(metallib_header(1, 26, 0))
            self.assertEqual(metallib_target(path), ('macosx', (26, 0)))
            path.write_bytes(b'#include <metal_stdlib>\n' + bytes(16))
            with self.assertRaises(ValueError): metallib_target(path)

    def test_library_for_a_newer_ios_is_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'a.metallib'
            path.write_bytes(metallib_header(2, 26, 0))
            check_metallib(path, 'iphoneos', '26.0')
            check_metallib(path, 'iphoneos', '27.0')
            with self.assertRaises(ValueError): check_metallib(path, 'macosx', '26.0')
            path.write_bytes(metallib_header(2, 27, 1))
            with self.assertRaises(ValueError): check_metallib(path, 'iphoneos', '26.0')

    def test_staging_refuses_shaders_for_a_newer_ios(self):
        with tempfile.TemporaryDirectory() as temp:
            root, out = Path(temp) / 'shaders', Path(temp) / 'generated'
            chain = root / 'ios' / 'b-abc'
            chain.mkdir(parents=True)
            (root / 'shader_map.tsv').write_text('package\n')
            (chain / 'k_b.metallib').write_bytes(metallib_header(2, 27, 1))
            with self.assertRaises(WorkspaceError): stage_shaders(root, out, 'abc', '26.0')
            self.assertFalse((out / 'ios').exists())
            (chain / 'k_b.metallib').write_bytes(metallib_header(2, 26, 0))
            stage_shaders(root, out, 'abc', '26.0')
            self.assertTrue((out / 'ios' / 'b-abc' / 'k_b.metallib').is_file())

    def test_tv_mode_audio_route_is_an_optional_boolean(self):
        data = json.loads((ROOT / 'games/rhythm-heaven/game.json').read_text())
        self.assertTrue(shell_tv_mode_audio_route(data['ios']))
        self.assertFalse(shell_tv_mode_audio_route({}))
        with self.assertRaises(WorkspaceError):
            shell_tv_mode_audio_route({'tv_mode_audio_route': 'yes'})


if __name__ == '__main__': unittest.main()
