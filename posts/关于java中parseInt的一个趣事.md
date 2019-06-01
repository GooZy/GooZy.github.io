---
title: '关于Java中parseInt的一个趣事'
date: 2016-11-24 23:19:00
tags: [Java]
published: true
hideInList: false
feature: 
---

今天看Java的时候突然好奇`parseInt()`的实现，想着会不会和自己平常比赛时候的实现方法一样。于是就翻到了这个：

<!--more-->

``` Java
public static int parseInt(String s, int radix)
                throws NumberFormatException
    {
        /*
         * WARNING: This method may be invoked early during VM initialization
         * before IntegerCache is initialized. Care must be taken to not use
         * the valueOf method.
         */

        if (s == null) {
            throw new NumberFormatException("null");
        }

        if (radix < Character.MIN_RADIX) {
            throw new NumberFormatException("radix " + radix +
                                            " less than Character.MIN_RADIX");
        }

        if (radix > Character.MAX_RADIX) {
            throw new NumberFormatException("radix " + radix +
                                            " greater than Character.MAX_RADIX");
        }

        int result = 0;
        boolean negative = false;
        int i = 0, len = s.length();
        int limit = -Integer.MAX_VALUE;
        int multmin;
        int digit;

        if (len > 0) {
            char firstChar = s.charAt(0);
            if (firstChar < '0') { // Possible leading "+" or "-"
                if (firstChar == '-') {
                    negative = true;
                    limit = Integer.MIN_VALUE;
                } else if (firstChar != '+')
                    throw NumberFormatException.forInputString(s);

                if (len == 1) // Cannot have lone "+" or "-"
                    throw NumberFormatException.forInputString(s);
                i++;
            }
            multmin = limit / radix;
            while (i < len) {
                // Accumulating negatively avoids surprises near MAX_VALUE
                digit = Character.digit(s.charAt(i++),radix);
                if (digit < 0) {
                    throw NumberFormatException.forInputString(s);
                }
                if (result < multmin) {
                    throw NumberFormatException.forInputString(s);
                }
                result *= radix;
                if (result < limit + digit) {
                    throw NumberFormatException.forInputString(s);
                }
                result -= digit;
            }
        } else {
            throw NumberFormatException.forInputString(s);
        }
        return negative ? result : -result;
    }
```



整体思路也是先乘基数，然后加值，多了对溢出的判断。在计算结果时，不是像我平常使用正数存储，而是默认是负数。不是很理解，然后注释说防止接近`MAX_VALUE`。发现：`INT_MAX = 2147483647 、 INT_MIN = -2147483648`。那么答案就很明显了，如果默认为正数的话，当值为`INT_MIN`时，会造成溢出，最终异常。好严谨Orz


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>

