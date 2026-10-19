# Touchable

**English** | [简体中文](README.zh-CN.md)

Touchable gives ported games a more native iOS experience. It improves touch controls, virtual buttons, graphics, and performance. Supply your own Switch game files. Build native iPhone games on an Apple Silicon Mac.

## Supported games

| Game | Game file version | Improvements |
| -------- | ------------------------ | ------------------------------------------------------------ |
| Rhythm Heaven | v0 (nsp) | Touch controls; HD rumble; virtual buttons cover less of the screen; more intuitive play and feedback; Liquid Glass buttons |
| Silksong | v0 (nsp) + v655360 (nsp) | Virtual button controls; HD rumble; adaptive widescreen; full resolution + 120 Hz |

## Get started

1. Install the full Xcode.
2. Put `prod.keys` in `MyGameFiles/keys/`.
3. Put each NSP in the folder for its game.
4. Double-click `Touchable.command`.
5. Select a game.
6. Select "Build and install" or "Build IPA only".

The first run needs a network connection. The launcher prepares the local tools.
The first signing needs your Apple Account in Xcode.
The launcher saves your local settings. You do not need to change internal configuration files.

## Where to find things

| Location | Purpose |
| --- | --- |
| [MyGameFiles](MyGameFiles/README.md) | Put your own NSP files and keys here |
| [IPA](IPA/README.md) | Find the finished install packages |
| [docs](docs/README.md) | Read the user guides |
| [internal](internal/README.md) | See the code and developer tools |

Game files, keys, personal settings, saves, and install packages stay on your Mac.
They do not go into Git.

For detailed requirements, see [Supported games](docs/supported-games.md).
For install steps, see [Signing and installation](docs/signing-and-install.md).
If an error occurs, first read [Troubleshooting](docs/troubleshooting.md).
Before development, read [AGENTS.md](AGENTS.md).
This project is based on [d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile).

## License and disclaimer

The code is under the [MIT License](LICENSE).

This project is not affiliated with or endorsed by Nintendo, Team Cherry, or any other game publisher.
It does not contain game files, keys, or firmware. You must supply files from games that you own.
Game names, logos, and artwork belong to their owners. The app icons and the Silksong logo in this repository are used only to identify the games.
