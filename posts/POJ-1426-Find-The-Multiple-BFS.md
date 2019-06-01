---
title: 'POJ 1426 Find The Multiple (BFS)'
date: 2016-04-17 13:01:46
tags: [BFS]
published: true
hideInList: false
feature: 
---

<font color="#6495ED">**题目链接：**</font>
[POJ 1426 Find The Multiple (BFS)](http://acm.pku.edu.cn/JudgeOnline/problem?id=1426)

<font color="#6495ED">**题意分析：**</font>  
给出一个数字n，查找一个只由0和1构成的数字，使得这个数字能够整除n。输出一个这样的数字。
<!--more-->

<font color="#6495ED">**解题思路：**</font>  
首先第一个数肯定是1，然后不断得枚举添加0或者1，用BFS进行搜索即可。这里要注意两点：  
1.长度很大的数字取余数可以使用从左到右解析的方式，所以每一次我们保留下解析后的余数即可，然后使用余数作为标记。  
2.这就要求我们需要另开一个数组来存答案，所以BFS里面存的是结构体。

<font color="#6495ED">**个人感受：**</font>  
不知道POJ上面那些肯定long long能存的下的人结论是哪里来的。想到了余数计算就行，却没想到怎么标记，加油~

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

struct P {
    char ans[111];
    int cnt;
    int mod;
};
bool vis[311];

int main()
{
    int n;
    while (~scanf("%d", &n) && n) {
        queue<P> q;
        memset(vis, 0, sizeof vis);
        P st;
        st.cnt = 1;
        st.ans[0] = '1';
        st.mod = 1 % n;
        q.push(st);

        while (q.size()) {
            P cur = q.front(); q.pop();
            if (cur.mod == 0) {
                for (int i = 0; i < cur.cnt; ++i) printf("%c", cur.ans[i]);
                putchar('\n');
                break;
            }
            vis[cur.mod] = 1;

            cur.cnt = cur.cnt + 1;
            cur.ans[cur.cnt - 1] = '0';
            cur.mod = (cur.mod * 10) % n;
            if (!vis[cur.mod])
                q.push(cur);
            cur.ans[cur.cnt - 1] = '1';
            cur.mod = (cur.mod + 1) % n;
            if (!vis[cur.mod])
                q.push(cur);
        }
    }
    return 0;
}

```


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

