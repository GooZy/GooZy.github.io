---
title: POJ 2763 Housewife Wind (LCA,RMQ,BIT)
date: 2016-04-17 13:08:31
tags: [LCA,RMQ,BIT]
categories: [ACM,数据结构]
---

<font color="#6495ED">**题目链接：**</font>
[POJ 2763 Housewife Wind (LCA,RMQ,BIT)](http://acm.pku.edu.cn/JudgeOnline/problem?id=2763)

<font color="#6495ED">**题意分析：**</font>  
给出两个操作，0：妈妈需要到树上某个结点接孩子，每次输出最短距离，然后妈妈的位置变成孩子所在的位置。1：更改树上某条边的距离为w。
<!--more-->

<font color="#6495ED">**解题思路：**</font>  
由于每次移动都会使得母亲的位置变动，这里我们需要使用LCA的在线算法。  
首先，我们将整棵树根据后序遍历拉成一条链，每次记录这个链上结点代表的结点是什么(vs[i])和深度是多少(dep[i])，顺便记录这个结点第一次出现的时候是在链上什么位置(id[i])。然后每次$lca(a,b)$其实就是查询$[id[a],id[b]]$这个区间内，dep最小的那个下标是什么。  
其次，由于本题涉及到更新操作，如上我们已经把它拉成一条链了，所以下一步只需在父亲指向儿子的边加权值，儿子指向父亲的边减权值，然后查询区间$$sum(id[a])+sum(id[b])-2 \times sum(id[lca(a,b)])$$即可。

<font color="#6495ED">**个人感受：**</font>  
爽呆了这题，为了A这题，A了两道RMQ，复习了BIT，爽23333

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
using namespace std;

const int MAXN = 1e5 + 111;

struct Edge {
    int to, id, w, next;
}edge[MAXN * 2];
int head[MAXN], tol;

void addedge(int u, int v, int id, int w) {
    edge[tol].to = v; edge[tol].w = w; edge[tol].id = id;
    edge[tol].next = head[u]; head[u] = tol++;
}

int s, bitn;
int w[MAXN];
vector<Edge> G[MAXN];

int id[MAXN], es[MAXN * 2], dep[MAXN * 2], vs[MAXN * 2];
int bit[MAXN * 2], dp[MAXN * 2][20];

void add(int i, int x) {
    while (i <= bitn) {
        bit[i] += x;
        i += lowbit(i);
    }
}

int sum(int i) {
    int ret = 0;
    while (i > 0) {
        ret += bit[i];
        i -= lowbit(i);
    }
    return ret;
}

void dfs(int u, int p, int sum, int &k) {
    id[u] = k;
    vs[k] = u;
    dep[k++] = sum;
    for (int i = head[u]; ~i; i = edge[i].next) {
        Edge &e = edge[i];
        if (e.to != p) {
            add(k, e.w);
            es[e.id * 2] = k;
            dfs(e.to, u, sum + e.w, k);
            vs[k] = u;
            dep[k++] = sum;
            add(k, -e.w);
            es[e.id * 2 + 1] = k;
        }
    }
}

int my_min(int a, int b) {
    return dep[a] <= dep[b] ? a : b;
}

void init_rmq(int n) {
    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 1; j < 20; ++j) {
        for (int i = 0; i + (1 << j) - 1 <= n; ++i) {
            dp[i][j] = my_min(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);
        }
    }
}

void init(int n) {
    bitn = n * 2 - 1;
    memset(bit, 0, sizeof bit);
    int k = 0;
    dfs(0, -1, 0, k);
    init_rmq(2 * n - 1);
}

int query(int l, int r) {
    int k = log2(r - l + 1);
    return my_min(dp[l][k], dp[r - (1 << k) + 1][k]);
}

int lca(int a, int b) {
    if (id[a] > id[b]) swap(a, b);
    return vs[query(id[a], id[b])];
}

int main()
{
    int n, q, u, v;
    while (~scanf("%d%d%d", &n, &q, &s)) {
        for (int i = 0; i < n; ++i) G[i].clear(), head[i] = -1;
        tol = 0;
        for (int i = 0; i < n - 1; ++i) {
            scanf("%d%d%d", &u, &v, &w[i]);
            --u, --v;
            addedge(u, v, i, w[i]);
            addedge(v, u, i, w[i]);
        }

        init(n);

        int op, a, b;
        --s;
        for (int i = 0; i < q; ++i) {
            scanf("%d%d", &op, &a);
            --a;
            if (op == 0) {
                int p = lca(s, a);
                printf("%d\n", sum(id[s]) + sum(id[a]) - 2 * sum(id[p]));
                s = a;
            }
            else {
                scanf("%d", &b);
                add(es[2 * a], b - w[a]);
                add(es[2 * a + 1], w[a] - b);
                w[a] = b;
            }
        }
    }
    return 0;
}

```



---

**广告时间**



> *VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>

