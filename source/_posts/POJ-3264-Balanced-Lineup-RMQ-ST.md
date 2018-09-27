---
title: POJ 3264 Balanced Lineup (RMQ,ST)
date: 2016-04-16 10:37:59
tags: [RMQ,ST]
categories: [ACM,数据结构]
---

<font color="#6495ED">**题目链接：**</font>
[POJ 3264 Balanced Lineup (RMQ,ST)](http://acm.pku.edu.cn/JudgeOnline/problem?id=3264)

<font color="#6495ED">**题意分析：**</font>  
询问区间$[L,R]$最大值和最小值的差值为多少?
<!--more-->

<font color="#6495ED">**解题思路：**</font>  
RMQ的ST算法登场。$dpl[i][j]$代表：从第i个数开始，包含第i个数，区间长度为$2^j$范围内的最小值。有转移：$$dpl[i][j] = min(dp[i][j - 1], dp[i + 2^{j - 1}][j - 1])$$
$dph[i][j]$同理。  
最终求区间中的最小值，那么我们只需查询:  
$k = log_2(r - l + 1)$  
$ans = min(dpl[i][k], dpl[i + (1 << k) + 1][k])$

<font color="#6495ED">**个人感受：**</font>  
头一次写ST算法，原来也不难啊......以前以为很复杂Orz

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
#define lowbit(x) (x & (-x))
#define ll long long
#define pr(x) cout << #x << " = " << (x) << '\n';
using namespace std;

const int INF = 0x7f7f7f7f;
const int MAXN = 5e4 + 111;

int dpl[MAXN][20], dph[MAXN][20], a[MAXN];

int getMax(int l, int r) {
    int k = log2(r - l + 1);
    return max(dph[l][k], dph[r - (1 << k) + 1][k]);
}

int getMin(int l, int r) {
    int k = log2(r - l + 1);
    return min(dpl[l][k], dpl[r - (1 << k) + 1][k]);
}

int main()
{
    int n, q;
    while (~scanf("%d%d", &n, &q)) {
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &a[i]);
            dpl[i][0] = dph[i][0] = a[i];
        }

        for (int j = 1; j < 20; ++j) {
            for (int i = 1; i <= n; ++i) {
                if (i + (1 << j) - 1 <= n) {
                    dpl[i][j] = min(dpl[i][j - 1], dpl[i + (1 << (j - 1))][j - 1]);
                    dph[i][j] = max(dph[i][j - 1], dph[i + (1 << (j - 1))][j - 1]);
                }
                else break;
            }
        }

        int l, r;
        for (int i = 0; i < q; ++i) {
            scanf("%d%d", &l, &r);
            printf("%d\n", getMax(l, r) - getMin(l, r));
        }
    }
    return 0;
}

```


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

