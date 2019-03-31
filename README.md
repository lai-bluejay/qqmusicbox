# QQMusicBox
[![Build Status](https://travis-ci.org/lai-bluejay/qqmusicbox.svg?branch=master)](https://travis-ci.org/lai-bluejay/qqmusicbox)
![PyPI](https://img.shields.io/pypi/v/diego.svg?style=flat)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/lai-bluejay/qqmusicbox.svg)

只要有声卡，命令行也能播放音乐


看到一款[命令行的网易云🎵](https://github.com/darknessomi/musicbox/)，忍不住想照着开发一个同款的QQ音乐，整体代码结构还是参考darkness的版本，在此版本上微调。qq音乐api会和[meik-h](https://github.com/MeiK-h/QQMusicAPI)一起维护

## 特性

暂时只支持搜索音乐.......

### 键盘快捷键

| Key   | Effect          |           |
| ----- | --------------- | --------- |
| j     | Down            | 下移        |
| k     | Up              | 上移        |
| h     | Back            | 后退        |
| l     | Forword         | 前进        |
| u     | Prev page       | 上一页       |
| d     | Next page       | 下一页       |
| f     | Search          | 快速搜索      |
| \[    | Prev song       | 上一曲       |
| ]     | Next song       | 下一曲       |
| =     | Volume +        | 音量增加      |
| -     | Volume -        | 音量减少      |
| Space | Play/Pause      | 播放/暂停     |
| m     | Menu            | 主菜单       |
| p     | Present/History | 当前/历史播放列表 |
| i     | Music Info      | 当前音乐信息    |
| ⇧+p   | Playing Mode    | 播放模式切换    |
| ⇧+a   | Enter album     | 进入专辑      |
| g     | To the first    | 跳至首项      |
| ⇧+g   | To the end      | 跳至尾项      |

## 安装

### 必选依赖

1.  `mpg123` 用于播放歌曲  自行搜索一下安装办法吧


### PyPi安装

    $ pip install qqmusicbox

### Git clone安装master分支

    $ git clone https://github.com/lai-bluejay/qqmusicbox.git && cd qqmusicbox
    $ python setup.py install

### macOS安装

    $ pip install qqmusicbox
    $ brew install mpg123

### Linux安装

#### Ubuntu/Debian

    $ (sudo) pip install qqmusicbox

    $ (sudo) apt-get install mpg123


#### Centos/Red Hat

    $ (sudo) pip(3) install qqmusicbox
    $ (sudo) wget http://mirror.centos.org/centos/7/os/x86_64/Packages/mpg123-1.25.6-1.el7.x86_64.rpm
    $ (sudo) yum install mpg123-1.25.6-1.el7.x86_64.rpm