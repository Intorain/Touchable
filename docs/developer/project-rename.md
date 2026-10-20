# Project rename

The project name is Touchable.
The previous name was Nitenphone.
This file is the only record of the previous identifiers.
Use the table below to read old reports, logs, and history entries.

## Full rename: 2026-10-20

This rename replaces all previous identifiers.
It changes Bundle IDs, the workspace directory, local state, and code identifiers.

| Item | Previous value | Current value |
| --- | --- | --- |
| Workspace directory | `~/DEV/Nitenphone` | `~/DEV/Touchable` |
| Local state directory | `.nitenphone/` | `.touchable/` |
| Isolated state setting | `NITENPHONE_STATE_DIR` | `TOUCHABLE_STATE_DIR` |
| Silksong Bundle ID | `com.mmmz.NitenphoneProbe` | `com.mmmz.TouchableSilksong` |
| Rhythm Heaven Bundle ID | `com.mmmz.NitenphoneSilksong` | `com.mmmz.TouchableRhythmHeaven` |
| Planned Rhythm Heaven Bundle ID | `com.mmmz.NitenphoneRhythmHeaven` | `com.mmmz.TouchableRhythmHeaven` |
| CPU probe Bundle ID | `com.mmmz.NitenphoneCPUProbe` | `com.mmmz.TouchableCPUProbe` |
| CPU probe target | `NitenphoneProbe` | `TouchableProbe` |
| Runtime macro | `NITENPHONE_SWITCH_RUNTIME` | `TOUCHABLE_SWITCH_RUNTIME` |
| Game interface header | `niten_game.h` | `touchable_game.h` |
| Game interface functions | `niten_game_*` | `touchable_game_*` |
| Generated configuration | `niten_game_config.h`, `NITEN_GAME_*` | `touchable_game_config.h`, `TOUCHABLE_GAME_*` |
| iOS identifiers | `Niten*` | `Touchable*` |
| Fallback font name | `NitenphoneFallback` | `TouchableFallback` |
| Generated Bundle ID prefix | `dev.nitenphone.user` | `dev.touchable.user` |

Product names and phone save paths do not change.
They stay `Silksong` and `RhythmHeaven`, and `Documents/Saves/<product>`.

### Effect on installed apps

iOS identifies an app by its Bundle ID.
The new Bundle IDs install as new apps.
The old apps stay on the device until you remove them.
The saves in the old apps do not move to the new apps.
Back up the saves from the old apps before the first install of a new build.
Restore the backup into the new apps after the install.
Signing needs provisioning profiles for the new Bundle IDs.

### Effect on local files

Reports, logs, and history entries before 2026-10-20 can contain the previous absolute paths.
Read `~/DEV/Nitenphone/.nitenphone/` as `~/DEV/Touchable/.touchable/` in these files.
Documentation and history entries use the current identifiers.
Read a Bundle ID in an old entry with the table above.
Signed apps and IPA files from before this rename keep the previous Bundle IDs.
The Python environment was rebuilt at the new path.
The Silksong first-run shader check runs again on the next build, because `nvn_mtl.m` changed.

## Branding rename: 2026-10-17

This rename changed the project name and the launcher filename only.
The launcher is `Touchable.command` at the repository root.
New private Mac transfer folders and ZIP names use the `Touchable-` prefix.
It kept all compatibility identifiers.
The 2026-10-20 rename replaced them.
