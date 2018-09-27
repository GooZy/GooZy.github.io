---
title: 图数据库Neo4j总结
date: 2017-11-16 23:34:58
tags: [总结]
categories: [学习,总结]
---

### 前言

最近业务上需要表现一些数据间的层级关系，考虑到关系型数据库的联表查询随着量级增大，复杂度骤增，打算采用图数据来存储这一部分数据用于展示。

<!--more-->

#### 介绍

Neo4j是一款开源的图形数据库，以图形结构的形式存储数据。

下载地址：<https://neo4j.com/download/other-releases/#releases>

解压后进入目录输入：`./bin/neo4j console` 即可启动，初始账号密码均为 neo4j

也可以直接在线尝试：<https://neo4j.com/sandbox-v2/?ref=product>

#### 与关系型数据库对比

![neo4j](http://7xsy54.com1.z0.glb.clouddn.com/image2017-11-16_15-44-14.png)

| 关系型数据库 | 图数据库                                     |
| ------ | ---------------------------------------- |
| 表      | 标签（每个节点都有自己所属的标签，标签内的节点可以看做一个组，单个节点可以拥有多个标签，上方财政部的标签就是Person） |
| 行      | 节点（节点记录着节点属性，单个节点拥有多个属性（建议越少越好，因为主要关注在点与点间关系上）） |
| 列      | 属性名                                      |
| 表间关系   | 节点间关系（关系带有标签，一个标签下可以有多个属性值，例如上方的参股就是一个关系标签） |
| SQL    | Cypher（专有查询语言）                           |

#### Cypher

总：<http://neo4j.com/docs/cypher-refcard/3.0/>

Cypher命令不区分大小写，但是属性值是区分的

**增**

```sql
CREATE (a:Person { name: "Guo", from: "China", age: 22 }),
(b:Person { name: "Zi", from: "China", age: 22 }),
(a)-[r:Knows {since: 1995}]->(b)
RETURN a, r, b
```

建立一个标签为Person，具有三个属性name、from、age的节点，a为变量名。然后建立两者的单向关系，其中Knows为关系标签，具有属性since。使用()来表示节点，{}表示节点属性

**查**

```sql
MATCH (a:Person), (b:Person)
WHERE a.name = "Guo" AND b.name = "Zi"
return a, b;
```

**删**

```sql
MATCH (b:Person)
WHERE  b.name = "Zi"
DETACH DELETE b;
```

DETACH会删除节点及与该节点相关的关系

**改**

```sql
MATCH (n)
where n.name='Guo'
set n.Company='Team'
return n;
```

#### 与Python交互

总：<https://neo4j.com/docs/api/python-driver/1.5/>

官方有提供驱动，但是我更推荐使用py2neo，使用起来更便捷

py2neo(3.0版本)：<http://py2neo.org/v3/>

**增删改查**

```python
from py2neo import Graph, Node, Relationship
 
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="000000"
)
 
 
# 增
father = Node('Person', name='A')
child = Node('Person', name='B')
graph.create(father)
graph.create(child)
graph.create(Relationship(father, 'Father_of', child))
# 改
father['name'] = 'C'
graph.push(father)
# 查
x = graph.find_one('Person', 'name', 'C')  # lable, key, value
# 删
graph.delete(x)
```

#### 关系数据库导入到图数据库

参考：<http://paradoxlife.me/how-to-insert-bulk-data-into-neo4j>

对于少量数据（文件必须放在neo4j的impot目录下）

```shell
load csv with headers from "file:///clue_invest.csv" as line
merge (p:Invest{company_name: line.company_name, name: line.name, level: line.level})
```

对于大量数据，可以考虑生成csv导入（header和数据分开有利于后期更改）

可以参考：<http://blog.csdn.net/macanv/article/details/78296066>

命令不要加多余空格，另外neo4j-import之后会考虑废弃，所以推荐使用neo4j-admin来进行

```bash
/Users/guoziyao/Desktop/neo4j-community-3.3.0/bin/neo4j-admin import --mode csv -nodes:Company company_header.csv,company.csv --nodes:Person person_header.csv,person.csv -relationships relationship.csv
```

#### 总结

以上便是这段时间学习的一个总结，更多的用法可以查看官方文档，以及给出的一些参考:)

---

**广告时间**


> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

