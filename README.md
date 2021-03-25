# README

## 简介

本脚本基于python的selenium，用pyinstaller打包成了可执行文件，作为练手的小程序，自动化操作浏览器打卡平安复旦，暂时定为8小时一打卡，简化无特殊情况下的平安复旦打卡工作，仅供学习交流使用，支持防疫工作，还请大家如实上报平安复旦。
## 使用方法
解压FudanDaily.zip,内含五个文件clockin.exe,clockin_Ninja_mode.exe,chromedriver.exe,README.md，usr.txt。

- README.md就是本文件，包含使用说明，常见问题的解决方法。
- clockin.exe是脚本的可执行文件（告诉你个小秘密，双击就可以启动了）
- clockin_Ninja_mode.exe无窗口后台模式启动。可以在任务管理器的进程中看到。
- chromedriver.exe是浏览器的驱动程序，对应目前最新的chrome89.0.4389.72（正式版本），大版本号不对是不能够使用的，会闪退，会闪退，会闪退！
- usr.txt保存你登录用的学号与密码，使用AES加密，请确保有这个文件，如果需要更改请手动删除文本内容。

双击clockin.exe会启动一个命令行窗口，第一次使用需要在命令框中输入账号密码，会自动加密保存在usr.txt中，下次启动自动填写。如需要更改把文本内容删除即可。登录成功后，每8小时自动打卡，全默认选项，位置定位为上海 杨浦区。

额外选项是在初次录入后，可以选择无窗口模式启动，即双击clockin_Ninja_mode.exe，程序会在后台运行。（请确保账号正确）

## 常见问题

### 黑窗闪退

chrome的版本是否正确？！现在的话更新到最新版即可，可以在浏览器的帮助——>关于google chrome里进行升级。

驱动程序是否与脚本在同一目录？

是否有中文路径？

如果以上都不符合，win+r 输入cmd回车，将exe程序拖入cmd窗口回车，看下报错信息，反馈给我掉头发用。

### 无法获取地理信息

建议更换网络环境，一般实验室的校园网会定位到上海市 杨浦区。如果无法定位，手动点一下？还是没办法获取位置的话那我就没法帮你了。

### 其他问题

谁知道呢，反正肯定会有的。

## 更新日志

### 1.0.1
- 提高程序长时间运行的稳定性，应该不再会在运行超过两天后卡死了
- 间歇断网兼容性，可以容忍中途断网程序正常运行（但是打不上卡），只要网络恢复打卡功能能够继续进行
- 浏览器窗口隐藏功能，现在浏览器默认是隐藏的了，不影响功能，打卡信息可以通过命令窗看到（如果无视大量垃圾信息的话……）
- 控制台无用信息隐藏，不管你舒服不舒服，我舒服了！
- 更新了透明背景的复旦图标，好看了又舒服了~~~
- 同时我自己老版本的程序被Windows Defender当成木马删除了一次（我……我……我木马我自己……啊这……），但是新版本暂时没有被拦截过，不知道是小概率误报还是啥。Windows Defender恐成稳定运行最大的敌人……请大家注意啦，这种打包好的程序加个后门超级容易，请不要从不信任渠道获取和使用，程序源码我也放github的SRC文件夹了，有兴趣大家可以自行下载运行。代码还写得比较烂，只是将将能用的程度，欢迎大家来提出建议。

有时间再去研究研究post的方法吧，看github也有其他人做了类似的脚本，有机会学习一个。有什么需求可以联系我。

### 1.0.2

- 考虑增加Edge的支持，想了想算了，好像不是刚需，还加大容量和出错率，鸽了。
- 根据大家的反馈，新增加无窗口模式启动，双击clockin_Ninja_mode.exe，启动忍者模式！~~按Q拔出龙刃~~ 无声息后台模式，不会有命令框，在任务管理器中能够看到一个内存占用大约是12M的进程在默默运行，不需要时可以结束进程关闭，其他一切功能与窗口模式一致。（请在窗口模式确认工作正常后再使用此模式）

### 2.0.0

- 加入了账号密码加密功能，在txt中不再是明文保存了，也不需要再手动修改txt，直接打开程序录入一次账号密码信息即可。如果需要重新录入账号密码，将usr.txt中的内容删除即可。
