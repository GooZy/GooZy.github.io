---
title: 从今天开始使用HyperComments啦！
date: 2017-03-22 20:16:24
tags: [HyperComments, 总结]
categories: [闲碎, 经验总结]
---

### 起因

[多说不再提供评论服务。](http://dev.duoshuo.com/threads/58d1169ae293b89a20c57241)

<!--more-->

### 为什么使用HyperComments

一开始我也是拒绝的，因为看原博客要改几个文件，嫌太麻烦（事实上改文件还不到10分钟，复制粘贴，over）。然后找了下国内的某些知名评论系统，下面是对比结果：

- 网易云跟帖
  - 评论会显示某某地区网友。
  - 注册站点竟然说已经被注册过 = =！
- 来必力
  - 无法使用邮箱进行匿名回复，只能社交账号登陆。
- 畅言
  - 注册的站点竟然要备案！
  - 还有网站注册系统，只能用手机号注册我也是醉了。
- 友言
  - 无法使用邮箱进行匿名回复，只能社交账号登陆。

#### HyperComments的缺点

1. 站点管理界面是英文，对于英语苦手体验不好。
2. 致命的缺点：**只能用google账号登录**(不能翻墙的童鞋绕行吧TAT)
3. 多说的评论导入不了。

#### HyperComments的优点

1. 免费版本最多支持每月100K的部件加载次数。换算成每天就是3333次的加载量，对于个人博客来说，我觉得还不错。
2. 界面简洁，没有XXX地区网友留言之类的头衔附加到留言处。
3. 支持填写邮箱进行回复，不需要强制登录第三方账号。
4. 支持emoji和回复添加附件 :)
5. 评论框不需要访客翻墙也能显示出来。(好像是家俄罗斯的公司，2333)

#### 总结

综上，我觉得HyperComments是这几个之中最好的。

### Next主题配置HyperComments

因为参考的教程是Next主题的，其它主题不知道行不行，看官请自便XD

#### 1. 登录官网，购买免费版本

官网链接：[https://www.hypercomments.com/pricing](https://www.hypercomments.com/pricing)

#### 2. 配置主题配置文件

再填写完必要信息后，会出现代码，其中第四行：`_hcwp.push({widget:"Stream", widget_id: xxxx});`，复制这个ID，打开主题配置文件`GooZy.github.io/themes/next/_config.yml`，加入如下描述：
```
# Hypercomments
hypercomments_id: xxxx
```

没找到ID的，可以登录到管理页面，点击设置按钮，打开左侧的Widget下的code即可看到代码。顺带一提：code下的General可以设置评论提醒，大家自行摸索吧XD

#### 3. 最终步骤：改写和添加文件

首先是文件`/themes/next/layout/_macro/post.swig`，打开后，在如下位置添加代码。其中**第5行到第16行**是新添代码，具体位置使用编辑器ctrl + f查找`<span class="post-comments-count disqus-comment-count" data-disqus-identifier="{{ post.path }}" itemprop="commentsCount"></span>`即可找到。
``` javascript
                <a href="{{ url_for(post.path) }}#comments" itemprop="discussionUrl">
                  <span class="post-comments-count disqus-comment-count" data-disqus-identifier="{{ post.path }}" itemprop="commentsCount"></span>
                </a>
              </span>
           {% elseif theme.hypercomments_id %}
           <!--noindex-->
              <span class="post-comments-count">
               &nbsp;|&nbsp;
                 <span class="post-meta-item-icon">
                   <i class="fa fa-comment-o"></i>
                   <a href="{{ url_for(post.path) }}#comments" itemprop="discussionUrl">
                     <span class="post-comments-count hc-comment-count" data-xid="{{ post.path }}" itemprop="commentsCount"></span>
                   </a>
                 </span>
             </span>
             <!--/noindex-->
            {% endif %}
          {% endif %}
```

接着修改`themes/next/layout/_partials/comments.swig`，**第8行到第9行**为新增代码
``` javascript
    {% elseif theme.disqus_shortname %}
      <div id="disqus_thread">
        <noscript>
          Please enable JavaScript to view the
          <a href="//disqus.com/?ref_noscript">comments powered by Disqus.</a>
        </noscript>
      </div>
    {% elseif theme.hypercomments_id %}
      <div id="hypercomments_widget"></div>
    {% endif %}
  </div>
{% endif %}
```

然后修改`themes/next/layout/_scripts/third-party/comments.swig`，**第3行**为新增代码
``` javascript
{% include './comments/duoshuo.swig' %}
{% include './comments/disqus.swig' %}
{% include './comments/hypercomments.swig' %}
```

最后新建文件`themes/next/layout/_scripts/third-party/comments/hypercomments.swig`，写入：
``` javascript
{% if not (theme.duoshuo and theme.duoshuo.shortname) and not theme.duoshuo_shortname and not theme.disqus_shortname %}

	{% if theme.hypercomments_id %}

		<script type="text/javascript">
		_hcwp = window._hcwp || [];

		_hcwp.push({widget:"Bloggerstream", widget_id: {{ theme.hypercomments_id }}, selector:".hc-comment-count", label: "{\%COUNT%\}" });

		{% if page.comments %}
		_hcwp.push({widget:"Stream", widget_id: {{ theme.hypercomments_id }}, xid: "{{ page.path }}"});
		{% endif %}

		(function() {
		if("HC_LOAD_INIT" in window)return;
		HC_LOAD_INIT = true;
		var lang = (navigator.language || navigator.systemLanguage || navigator.userLanguage || "en").substr(0, 2).toLowerCase();
		var hcc = document.createElement("script"); hcc.type = "text/javascript"; hcc.async = true;
		hcc.src = ("https:" == document.location.protocol ? "https" : "http")+"://w.hypercomments.com/widget/hc/{{ theme.hypercomments_id }}/"+lang+"/widget.js";
		var s = document.getElementsByTagName("script")[0];
		s.parentNode.insertBefore(hcc, s.nextSibling);
		})();
		</script>

	{% endif %}

{% endif %}
```

好啦！大功告成~然后就可以去DIY下HyperComments的后台管理，探索新大陆啦~

代码部分有看不懂的，可以看下方参考资料的代码。

### 参考资料

1. [Гиперкомментарии для темы Next в Hexo](https://almostover.ru/2016-10/add-hypercomments-to-hexo-theme-next/)


---

**广告时间**




> *Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>

> *VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://www.vultr.com/media/banner_2.png)</a>

