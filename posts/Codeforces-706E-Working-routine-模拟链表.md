---
title: 'Codeforces 706E Working routine (模拟链表)'
date: 2016-08-12 23:31:40
tags: [链表,实现,数据结构]
published: true
hideInList: false
feature: 
---

### 题目链接：

[Codeforces 706E Working routine (模拟链表)](http://codeforces.com/problemset/problem/706/E)

### 题意分析：

给出一个矩阵和q个操作，每次操作需要交换矩阵的两个子矩形，问：经过q次操作后，最终矩阵长什么样子。

<!--more-->

### 解题思路：

$1000 \times 1000$ 的矩阵啊，$n^{2}$ 操作肯定是要T的。考虑链表将整个矩阵串在一起，如下图：

![](http://7xsy54.com1.z0.glb.clouddn.com/Codeforces%20706E%20Working%20routine.png)

发现对于任意需要我们交换的矩阵，其实我们只需要改变这两个矩阵的周围一圈元素的指针指向即可完成两个矩阵的交换。单次操作复杂度就降到了O(n + m)了。另外我们只需要知道元素的右边下边是什么，并不用关心上方，左方是什么，所以只用存储两个方向即可。

### 个人感受：

链表赛高！

### 具体代码链接：

[传送门](https://github.com/GooZy/Codes/blob/master/OJ-Codeforces/%23367%20div2/Working%20routine.cpp)


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

