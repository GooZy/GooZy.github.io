---
title: 'Arnold变换(附Python实现)'
date: 2018-04-29 19:34:06
tags: [图像]
published: true
hideInList: false
feature: 
---

### 介绍

首先是一个概念：置乱。意即将图像的信息次序打乱，使其变换成杂乱无章难以辨认的图像。

用处大概就是：对图像加个密，除非你暴力破解，否则你不知道这是个啥。~~所以就能安心地在百度云上存些蜜汁图片~\(≧▽≦)/~啦~~

<!--more-->

### Arnold变换

也叫做猫脸变换，因为提出该算法的人当时是在一张猫的图片上操作，因此而得名= =

这个变换公式很简单：

![公式](https://user-images.githubusercontent.com/12698567/39406471-c4080f28-4be9-11e8-99f6-42f9a190093c.jpg)

这里N代表图像的长宽，意即需要是正方形。当然，如果你想在长方形上尝试，把长方形切割成多个正方形，分别对正方形操作即可。Xn和Yn是原图像像素点位置，Xn+1和Yn+1该像素点的新位置。

有两点十分神奇，我也不知道为什么：

1. 单次变换后，所有像素点一一映射，也就是单映射。
2. 经过一定的变换次数后，图像会变换成原来的样子。

### 算法实现大致思路

原图到新图就不说了，直接照着公式来。还原的话，只需要在公式两边乘上逆矩阵即可。

具体可以看代码的arnold和iarnold部分：[传送门](https://github.com/GooZy/EasyW/blob/master/easyw/common/utils.py)

### 参考资料

1. [Arnold变换置乱图像](https://blog.csdn.net/yezi_happy/article/details/52804574)
2. [python中有关矩阵的创建、求逆、转置](https://blog.csdn.net/shuaishuai3409/article/details/50830196)
3. [百度百科：置乱](https://baike.baidu.com/item/%E7%BD%AE%E4%B9%B1/6575561?fr=aladdin)


---

**广告时间**

> Java学习网站: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

