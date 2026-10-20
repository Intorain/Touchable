# Rhythm Heaven IPA

This folder holds the current Rhythm Heaven package and its checksum records.
The current package is build 35.
It supports iPhone, iPad, a separate in-game language setting, controller haptics, and a live border glow.
The touch buttons use Liquid Glass.
Build 35 fixes the Simplified Chinese per-app language mapping.
The current IPA is `RhythmHeaven-build35-language-20261020.ipa`.
Its SHA-256 is `eeafd2560a91e419b03d771fae47bc36b4cc7739110c57876aca2c2f20bf7c83`.
The local IPA is unsigned. Sign it with PlayCover or another installation tool before use.
Build 35 reuses the build 34 patched modules, shaders, and RomFS. The reused shader chain is `98bab944ce89`.
No device test was run.
Build 29 fixes BeatSpell performance and touch.
Build 30 rewrites the border glow to make the light more natural. Build 31 makes the letterbox border follow the picture faster. Build 32 makes the transition between the picture edge and the letterbox border smoother. Build 33 declares Game Mode and stays at 60 Hz. In build 34, a pressed glass button shows only the system effect.
The build 34 IPA is `RhythmHeaven-build34-glass-press-20261019.ipa`.
Its SHA-256 is `e00e8817f69e5ebfd2b4ec856bb7e4f65bf3f44b797debbededd65ea8a7f27c0`.
Build 34 was checked only on the Mac host, in unit tests, and in the Simulator. It is not installed on a device yet.
The iPhone has build 30. The iPad mini has build 27.
Controller haptics are verified only on the iPad mini with a DualSense.
The build 33 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build34/`.
The build 32 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build33/`.
The build 31 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build32/`.
The build 30 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build31/`.
The build 29 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build30/`.
The build 28 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build29/`.
The build 27 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build28/`.
The build 26 IPA, JSON, and SHA-256 moved to `.nitenphone/archive/ipa/rhythm-heaven/before-build27/`.
The build 19 and build 20 IPA, JSON, and SHA-256 stay in `.nitenphone/archive/ipa/rhythm-heaven/before-build26/`.
The language setting is at "Settings > Apps > Rhythm Heaven > Language".
Close the game on the device. Then install with "Install existing IPA" in the top-level launcher.
The launcher build actions currently refuse Rhythm Heaven. For the reason, see the known limits in `internal/games/rhythm-heaven/README.md`.
