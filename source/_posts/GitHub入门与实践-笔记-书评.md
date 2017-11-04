---
title: GitHub入门与实践 笔记+书评
date: 2016-11-23 14:35:04
tags: [git, 笔记, 开源]
categories: [学习, 笔记]
---

### 笔记

-  `git diff HEAD` (查看本次提交和上次提交的区别)

-  `git reset --hard hashValue` 回退到哈希值对应版本。这条命令会把你工作目录中所有未提交的内容清空(当然这不包括未置于版控制下的文件 untracked files)

-  `git checkout -- xx.txt` 恢复单个文件

-  `git commit --amend` 修改最近一次的提交信息

-  `git commit -am '...'` 个别文件修改时，直接这样，省事。

   <!--more-->

-  **分支操作**
   - `git branch` (显示分支一览表)
   - `git branch xxx` (创建分支xxx)
   - `git checkout xxx` (切换到分支xxx)
   - `git checkout -b xxx` (上方两命令的合成)
   - `git checkout -` (切换回上一个分支)
   - `git merge --no-ff xxx` (合并xxx到当前分支，关闭fast-forward，保留commit历史)
   - `git branch -D xxx` 删除分支xxx
   - `git branch -a` (查看所有分支)
   - `git branch -r` (查看远程分支)

-  `git reflog` (查看当前仓库的操作日志)

-  发送pull request
   - 首先网页上fork
   - 然后`git clone git@github.com:username/proName`
   - 创建特性(Topic)分支。
      - `git checkout -b work xxx`(xxx为源分支)
   - 修改文件
   - `git diff`查看修改是否正确进行
   - 全部确认完毕后提交到本地仓库。`git add xxx` 和 `git commit -m 'xxx'`
   - 由于目前只建立了本地的分支work，还需在远程建立此分支。`git push origin work` 在远程建立这个分支。
   - 从网页进入分支。提交PR

-  `git fetch xxx` 更新分支xxx到最新版本。此时需要手动进行merge。这种做法比较安全

-  接收pull request
   - 首先，我们把**接收方**仓库clone到本地。已经clone过的，就通过pull更新到最新版。
   - 然后，把**发送方**的仓库设置为远程仓库(`git remote add name git@github.com:prSender/repoName`)。接着fetch到本地。
   - 建立一个分支merge刚才fetch的内容。接着就是看看程序是否没有问题。
   - 没问题，你就把这个分支删了吧。
   - 最后到网页接收PR即可。
      - 当然，也可以切换到主分支，进行合并，然后push到github，此时PR会自动关闭。

-  与github相互协作的工具或服务

   - hub。完全包含git的所有命令，并且对其进行了简化和扩展。
   - Travis CI(Continuous Integration)。可以在开发者执行提交后立即进行测试和构建。Travis Weblint检查配置文件.travis.yml是否错误。有些仓库的readme中显示有些条状状态，正是Travis CI的测试结果的显示。
   - Coveralls。代码覆盖率检测服务。
   - Gemnasium。查询github仓库正在使用的RubyGems或npm(Node Package Manager)，让开发者了解自己是否正在使用新版本进行开发。
   - Code Climate。只支持Ruby，提供代码分析报告服务，对代码质量进行评定，指出质量有问题代码。收费。
   - Jenkins。持续集成开发服务。主要用于持续、自动地构建/测试软件项目和监控一些定时执行的任务。


### 书评

这本书可以算是一本**工具书**+**经验书**。  书中有很多的命令，所以记笔记是必须的。另外作者也会根据自己的经历给出一些开发中需要注意的事项。对于入门而言我觉得是极好的一本书，剩下的提高就要看自己之后的实践了。此外书不大，作为参考书放着也是极好的。


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

