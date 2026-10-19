# Touchable

[English](README.md) | **简体中文**

本项目致力于给移植游戏做出更贴近 iOS 原生的游戏体验，包括但不限于优化触摸操作、虚拟按键、画面和性能。请使用自己提供的相关 Switch 游戏文件，在 Apple Silicon Mac 上构建 iPhone 原生游戏。

## 适配游戏列表

| 游戏     | 游戏文件版本             | 优化改进                                                     |
| -------- | ------------------------ | ------------------------------------------------------------ |
| 节奏天国 | v0 (nsp)                 | 支持触摸操作；HD 震动；减少虚拟按键遮挡；更直觉的游玩方式和反馈；液态玻璃按键 |
| 丝之歌   | v0 (nsp) + v655360 (nsp) | 虚拟按键操作；HD 震动；自适应宽屏；全分辨率+120hz            |

## 开始使用

1. 安装完整的 Xcode。
2. 将 `prod.keys` 放入 `MyGameFiles/keys/`。
3. 将 NSP 放入对应的游戏目录。
4. 双击 `Touchable.command`。
5. 选择游戏。
6. 选择 “Build and install”（构建并安装）或 “Build IPA only”（仅构建 IPA）。

首次运行需要网络连接。启动器会准备本机工具。
首次签名需要在 Xcode 登录你的 Apple 账户。
启动器会保存本机设置。你不需要修改内部配置文件。

## 文件入口

| 位置 | 用途 |
| --- | --- |
| [MyGameFiles](MyGameFiles/README.md) | 放入自己的 NSP 和密钥 |
| [IPA](IPA/README.md) | 查找构建完成的安装包 |
| [docs](docs/README.md) | 阅读使用说明（英文） |
| [internal](internal/README.md) | 查看代码和开发工具 |

游戏文件、密钥、个人设置、存档和安装包只保存在本地。
它们不进入 Git。

详细要求见 [支持游戏](docs/supported-games.md)。
安装步骤见 [签名和安装](docs/signing-and-install.md)。
遇到错误时，先看 [常见问题](docs/troubleshooting.md)。
开发前请阅读 [AGENTS.md](AGENTS.md)。
详细文档和启动器界面使用英文。
参考项目为 [d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)。

## 许可和声明

代码使用 [MIT 许可证](LICENSE)。

本项目与任天堂、Team Cherry 或其他游戏发行商无关，也未获得其认可。
本项目不包含游戏文件、密钥或固件。请使用你自己拥有的游戏文件。
游戏名称、标志和美术素材归其各自所有者。仓库中的应用图标和丝之歌标志仅用于标识游戏。
