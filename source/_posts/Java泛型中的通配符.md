---
title: Java泛型中的通配符
date: 2017-03-20 19:11:05
tags: [Java, 泛型]
categories: [学习, 笔记]
---

最近想学学集合框架的源代码，结果画风是这样的：

``` Java
boolean addAll(Collection<? extends E> c);
default boolean removeIf(Predicate<? super E> filter) {
	...
}
boolean containsAll(Collection<?> c);
```

一下就暴露了泛型没好好学的锅= =，今天总结一下。

<!--more-->

下文统一使用这两个类进行说明。

``` Java
class Fruit {}
class Apple extends Fruit {}
```

### 泛型中的通配符

#### 上边界限定通配符

用法：`<? extends Fruit>`

即当前类型 `X = ? extends Fruit`，类似`X <= Fruit`的感觉

这个X类型，表示是某个Fruit子类(或者Fruit本身)的类型，这也就意味着X类型有多种可能性，而编译器无法判定是哪一个类型，所以通过这种方法声明的List无法添加元素，只允许取出元素，取出的元素全都会向上转型。

#### 下边界限定通配符/超类型的通配符

用法：`<? super Fruit>`

即当前类型 `X = ? super Fruit`，类似`X >= Fruit`的感觉

这里的X类型，表示是某个Fruit父类(或者Fruit本身)的类型，虽然这里的X的类型也有多种可能性，但是编译器可以断定，只要加入的类型是Fruit子类或者Fruit本身，就一定可以向上转型。所以通过这种方法声明的List允许添加Fruit及其子类型的对象，加入的对象会自动向上转型成Fruit。

与上边界通配符的配合：
``` Java
class Test {
    public static <T> void copy(List<? super T> dest, List<? extends T> src) {
        for (int i = 0; i < src.size(); i++)
            dest.set(i, src.get(i));
    }
}
```

#### 无边界通配符

用法：`<?>`

即当前类型X不限定范围，可能是任意的一个类型。所以自然也就无法向其添加任何元素了。用法类似于`extends`，不过`get`出来的是`Object`类型就是了。

### PS

引子中的`removeIf`是一个默认方法，不得不赞一发，既扩展了接口方法，又不使得实现接口的类去添加新方法的覆盖，具体见参考资料。之后别人再问接口和抽象类的区别，就不能说普通类实现接口一定要实现所有方法了，2333。

### 参考资料

1. [Java 泛型总结（三）：通配符的使用](https://segmentfault.com/a/1190000005337789#articleHeader0)
2. [Java 8 默认方法（Default Methods）](http://ebnbin.com/2015/12/20/java-8-default-methods/)



---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

