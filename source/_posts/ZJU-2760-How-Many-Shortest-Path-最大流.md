---
title: ZJU 2760 How Many Shortest Path (最大流)
date: 2016-04-15 05:40:00
tags: [最大流]
categories: [ACM,图论]
---

<font color="#6495ED">**题目链接：**</font>[ZJU 2760 How Many Shortest Path (最大流)](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=2760)

<font color="#6495ED">**题意分析：**</font>

求从指定点到指定点的没有重边的最短路个数。如果起点终点相同，则输出“inf”。
<!--more-->

<font color="#6495ED">**解题思路：**</font>

将最短路上的所有边都保留下来，求最大流即可。注意：本题i == j 时，不一定矩阵就是0，坑爹啊。

<font color="#6495ED">**个人感受：**</font>

首先是我一直以为流量为0输出inf，没想到这样判断就T成傻逼。。。。。还以为是floyd的锅！通过此，又对自己的板子加深了理解XD。mp[i][i]不一定为0也是醉了。

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

const int MAXN = 210;//点数的最大值
const int MAXM = 20000;//边数的最大值
const int INF = 0x3f3f3f3f;

struct Edge
{
    int to,next,cap,flow;
}edge[MAXM];//注意是MAXM
int tol, src, des;
int head[MAXN];
int gap[MAXN],dep[MAXN],pre[MAXN],cur[MAXN];

void init()
{
    tol = 0;
    memset(head,-1,sizeof(head));
}
//加边，单向图三个参数，双向图四个参数
void addedge(int u,int v,int w,int rw=0)
{
    edge[tol].to = v;edge[tol].cap = w;edge[tol].next = head[u];
    edge[tol].flow = 0;head[u] = tol++;
    edge[tol].to = u;edge[tol].cap = rw;edge[tol].next = head[v];
    edge[tol].flow = 0;head[v]=tol++;
}
//输入参数：起点、终点、点的总数
//点的编号没有影响，只要输入点的总数
int sap(int start,int end,int N)
{
    memset(gap,0,sizeof(gap));
    memset(dep,0,sizeof(dep));
    memcpy(cur,head,sizeof(head));
    int u = start;
    pre[u] = -1;
    gap[0] = N;
    int ans = 0;
    while(dep[start] < N)
    {
        if(u == end)
        {
            int Min = INF;
            for(int i = pre[u];i != -1; i = pre[edge[i^1].to])
            if(Min > edge[i].cap - edge[i].flow)
                Min = edge[i].cap - edge[i].flow;
            for(int i = pre[u];i != -1; i = pre[edge[i^1].to])
            {
                edge[i].flow += Min;
                edge[i^1].flow -= Min;
            }
            u = start;
            ans += Min;
            continue;
        }
        bool flag = false;
        int v;
        for(int i = cur[u]; i != -1;i = edge[i].next)
        {
            v = edge[i].to;
            if(edge[i].cap - edge[i].flow && dep[v]+1 == dep[u])
            {
                flag = true;
                cur[u] = pre[v] = i;
                break;
            }
        }
        if(flag)
        {
            u = v;
            continue;
        }
        int Min = N;
        for(int i = head[u]; i != -1;i = edge[i].next)
            if(edge[i].cap - edge[i].flow && dep[edge[i].to] < Min)
            {
                Min = dep[edge[i].to];
                cur[u] = i;
            }
        gap[dep[u]]--;
        if(!gap[dep[u]])return ans;
        dep[u] = Min+1;
        gap[dep[u]]++;
        if(u != start) u = edge[pre[u]^1].to;
    }
    return ans;
}

int mp[MAXN][MAXN], dp[MAXN][MAXN];

void floyd(int n) {
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (dp[i][k] == INF) continue;
            for (int j = 0; j < n; ++j) {
                if (dp[k][j] == INF) continue;
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
            }
        }
    }
}

int main()
{
    int n;
    while (~scanf("%d", &n)) {
        init();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                scanf("%d", &mp[i][j]);
                if (i == j) mp[i][j] = 0;
                dp[i][j] = mp[i][j];
                if (mp[i][j] == -1) dp[i][j] = INF;
            }
        }
        scanf("%d%d", &src, &des);

        floyd(n);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mp[i][j] == -1) continue;
                if (dp[src][des] == dp[src][i] + mp[i][j] + dp[j][des]) {
                    addedge(i, j, 1);
                }
            }
        }

        if (src == des) printf("inf\n");
        else printf("%d\n", sap(src, des, n));
    }
    return 0;
}

```


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

