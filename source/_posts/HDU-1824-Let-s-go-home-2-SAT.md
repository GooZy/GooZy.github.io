---
title: "HDU 1824 Let's go home (2-SAT)"
date: 2016-04-25 20:47:38
tags: [tarjan, 2-SAT]
categories: [ACM,图论]
---

<font color="#6495ED">**题目链接：**</font>
[HDU 1824 Let's go home (2-SAT)](http://acm.hdu.edu.cn/showproblem.php?pid=1824)

<font color="#6495ED">**题意分析：**</font>  
n支队伍，m个关系。满足：1.队伍里面，队长和其余两名队员两者中必须有一个要留下来；2.关系中，A队员留下B队员就得离开，B队员留下，A队员就要离开。问：能否合理安排满足以上两个关系。
<!--more-->

<font color="#6495ED">**解题思路：**</font>  
将每个点拆分成两种状态：留下和不留下，然后根据题目，设：A为队长，B和C为队员，那么就有!A->(B^C), (!Bv!C)->A, 然后每个关系中，有：B->!C, C->!B. 最终根据关系建边，判断矛盾关系是否在同一个连通分量内即可。  
2-SAT类型的题，重要的就在于把这些对象间的关系理清楚。

<font color="#6495ED">**个人感受：**</font>  
这题充分考验了ACMer的语文水平，唉唉唉。

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
#define ll long long
#define pr(x) cout << #x << " = " << (x) << '\n';
using namespace std;

const int INF = 0x7f7f7f7f;
const int MAXN = 6e3 + 111;

vector<int> G[MAXN];
int n, m;
int dfn[MAXN], low[MAXN], sta[MAXN], id[MAXN], indx, scc, top;
bool in[MAXN];

void init() {
    for (int i = 0; i <= 6 * n; ++i) {
        G[i].clear();
        in[i] = 0;
        dfn[i] = 0;
    }
    indx = scc = top = 0;
}

void tarjan(int u) {
    dfn[u] = low[u] = ++indx;
    sta[top++] = u;
    in[u] = 1;
    for (int i = 0; i < G[u].size(); ++i) {
        int v = G[u][i];
        if (!dfn[v]) {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        }
        else if (in[v]) low[u] = min(low[u], dfn[v]);
    }

    if (dfn[u] == low[u]) {
        ++scc;
        int v;
        do {
            v = sta[--top];
            in[v] = 0;
            id[v] = scc;
        } while (v != u);
    }
}

int main()
{
    int a, b, c;
    while (~scanf("%d%d", &n, &m)) {
        init();
        int add = 3 * n;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d", &a, &b, &c);
            G[a + add].push_back(c);
            G[a + add].push_back(b);
            G[b + add].push_back(a);
            G[c + add].push_back(a);
        }
        int u, v;
        while (m --) {
            scanf("%d%d", &u, &v);
            G[u].push_back(v + add);
            G[v].push_back(u + add);
        }

        for (int i = 0; i < 6 * n; ++i) {
            if (!dfn[i]) tarjan(i);
        }

        bool flag = 1;
        for (int i = 0; i < 3 * n; ++i) {
            if (id[i] == id[i + 3 * n]) {
                flag = 0;
                break;
            }
        }
        printf("%s\n", flag? "yes" : "no");
    }
    return 0;
}

```


---

**广告时间**

> *VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>

> *QQ自助代刷*: <a href="http://qqzzds.hxcvb.com/" target="_blank">![qqzzds](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/qqzzds.png?raw=true)</a>

