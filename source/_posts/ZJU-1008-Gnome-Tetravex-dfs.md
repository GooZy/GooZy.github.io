---
title: ZJU 1008 Gnome Tetravex (DFS)
date: 2016-04-20 14:00:49
tags: [DFS]
categories: [ACM,图论]
---

<font color="#6495ED">**题目链接：**</font>
[ZJU 1008 Gnome Tetravex (DFS)](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1008)

<font color="#6495ED">**题意分析：**</font>  
给出$N \times N$块正方形，每一块被切割成上下左右四个三角形，每个三角形写上0~9的值，问：能否移动这些正方形的位置，使得它们排列成$N \times N$的方块，每一个相邻的边上数字都相同。
<!--more-->

<font color="#6495ED">**解题思路：**</font>  
从第一个方块开始枚举，还必须加上必要的剪枝，比如规格相同的方块在同一个地方不可行一次就不用试第二次了。

<font color="#6495ED">**个人感受：**</font>  
啊啊啊，剪枝想不到啊啊啊啊啊。。。

<font color="#6495ED">**具体代码如下：**</font>  

```c++
#include<algorithm>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#define pr(x) cout << #x << " = " << (x) << '\n';
using namespace std;

struct Square {
    int u, r, d, l;
}sq[30];
int mp[10][10], sum[30];
int n, ed;

bool dfs(int p) {
    if (p == ed) {
        return 1;
    }

    int x = p / n, y = p % n;
    for (int i = 0; i < ed; ++i) {
        if (!sum[i]) continue;
        if (x > 0 && sq[mp[x - 1][y]].d != sq[i].u) continue;
        if (y > 0 && sq[mp[x][y - 1]].r != sq[i].l) continue;
        mp[x][y] = i;
        --sum[i];
        if (dfs(p + 1)) return 1;
        ++sum[i];
    }
    return 0;
}

int main()
{
    int kase = 0;
    while (~scanf("%d", &n) && n) {
        ed = n * n;
        for (int i = 0; i < ed; ++i) {
            sum[i] = 0;
            scanf("%d%d%d%d", &sq[i].u, &sq[i].r, &sq[i].d, &sq[i].l);
            bool flag = 1;
            for (int j = 0; j < i; ++j) {
                if (sq[i].u == sq[j].u && sq[i].r == sq[j].r
                    && sq[i].d == sq[j].d && sq[i].l == sq[j].l) {
                    ++sum[j];
                    flag = 0;
                    break;
                }
            }
            if (flag) sum[i] = 1;
        }

        if (kase) putchar('\n');
        if (dfs(0)) printf("Game %d: Possible\n", ++kase);
        else printf("Game %d: Impossible\n", ++kase);
    }
    return 0;
}

```


---

**广告时间**

> *VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>

> *QQ自助代刷*: <a href="http://qqzzds.hxcvb.com/" target="_blank">![qqzzds](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/qqzzds.png?raw=true)</a>

