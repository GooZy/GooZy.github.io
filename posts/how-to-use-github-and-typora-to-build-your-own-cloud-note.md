---
title: '如何用github和typora打造自己的云笔记'
date: 2019-03-10 18:21:55
tags: [总结]
published: true
hideInList: false
feature: 
---

## 缘起

从2016年冬季开始，我就有了看书会记些笔记的习惯，在比对了各个软件之后，选定了有道云笔记。主要看中了：1.免费；2.跨多个平台（手机、mac、windows）；3.可以用markdown写。

<!--more-->

这几年用下来，确实也还不错。但总有一些让我不满意的地方，一是有时候卡顿严重，几乎无法书写；二是笔记的版本管理，我在mac上使用时，查看笔记的版本，虽然软件提供了比对近30天版本的功能，但是我发现各版本的区别就是0和1的区别（下图显示3-5号和3-3号两版本没任何改动，但其实我本身是有改动的）；三是我怕某天笔记倒闭了我这几年的笔记就得一个一个慢慢下载下来了，十分被动；最后一点就是有道云笔记支持不了本地图片添加到markdown里面；

![版本比较](https://user-images.githubusercontent.com/12698567/54083766-4631c180-4363-11e9-8a4d-955405592a4c.png)

所以渐渐地，我也有了把笔记上传github的想法。可是彼时github私有仓库是收费的，而我又不想私密的笔记公开，所以就作罢。但是现在不一样了，github私有仓库免费了，所以我也开始着手自己的转移工作。

## 所需工具

- git，官网传送门：[点我](https://git-scm.com/)
  - 开源的分布式版本控制系统
- Typora，官网传送门：[点我](https://www.typora.io/)
  - Typora是一个本地的[markdown](https://baike.baidu.com/item/markdown/3245829?fr=aladdin)编辑工具，支持Windows/Mac/Linux三大系统

## 步骤

#### 1. 建立自己的github私有仓库

进入github官网，在个人仓库页面，新建私人仓库。

![私有仓库](https://user-images.githubusercontent.com/12698567/54084273-b04d6500-4369-11e9-9fb3-c8ea4445ea9c.png)

#### 2. 克隆到本地

然后进入项目页面，克隆仓库到本地。

![克隆1](https://user-images.githubusercontent.com/12698567/54084286-d07d2400-4369-11e9-9f58-4e2cc35d3a58.png)

![克隆2](https://user-images.githubusercontent.com/12698567/54084287-d1ae5100-4369-11e9-894d-8ab8b90a53e9.png)

#### 3. 设置Typora

主要就是开启Typora的文件树视图。

![t1](https://user-images.githubusercontent.com/12698567/54084318-1639ec80-436a-11e9-8f43-8b41abe2a338.png)

然后打开你的仓库。

![t2](https://user-images.githubusercontent.com/12698567/54084319-1639ec80-436a-11e9-816a-cbfd7c72f881.png)

![t3](https://user-images.githubusercontent.com/12698567/54084320-176b1980-436a-11e9-95d6-21778630c3e1.png)

之后所有的新建文件、目录操作都可以在文件树视图里面进行，不小心关闭了软件，只需要打开最近打开的文件，目录树自动就加载出来了。

## 总结

**优点**

1. 本地图片放到同级目录下，就可以使用相对路径引入，在本地看笔记很方便。
2. 所有笔记都在本地，同步到github，具有版本控制。
3. 本地编辑，十分流畅。

**缺点**

1. 同步github比较麻烦，需要自己提交至github。（可以自己写个crontab命令进行定时检测仓库变动，然后上传github）
2. 笔记的分享功能没有了。（这个我个人的解决方式是发布到[ubuntu pastebin](https://paste.ubuntu.com/)进行分享，本来是想推荐gist的，结果被墙了=。=)