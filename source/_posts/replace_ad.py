# -*- coding: utf-8 -*-
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
import glob

ad = [
    '*VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>',
    '*QQ自助代刷*: <a href="http://qqzzds.hxcvb.com/" target="_blank">![qqzzds](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/qqzzds.png?raw=true)</a>',
    '*VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://www.vultr.com/media/banner_2.png)</a>',
]

new_ad = {
    '*Java学习网站*: <a href="http://how2j.cn?p=23251" target="_blank">![how2j](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/how2j.png?raw=true)</a>': 0,
    '*VPS*: <a href="https://www.vultr.com/?ref=7255071" target="_blank">![VPS](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/banner_2.png?raw=true)</a>': 0,
}

def delete_ad():
    for filename in glob.glob('*.md'):
    	outs = ''
        with open(filename, 'r') as f:
            lines = f.readlines()
            skip = False
            for line in lines:
            	if skip:
            		skip = False
            		continue
            	for each in ad:
            		if each in line:
            			skip = True
            			break
            	else:
            		outs += line
        with open(filename, 'w') as f:
            f.writelines(outs)

            
def init_ad():
    for filename in glob.glob('*.md'):
        has = False
        with open(filename, 'r') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if u'广告时间' in line:
                    has = True
                    break
        if not has:
            lines.append(u'\n\n\n---\n\n**广告时间**\n\n')
            with open(filename, 'w') as f:
                f.writelines(lines)


def add_ad():
    for filename in glob.glob('*.md'):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                for k in new_ad:
                    if k in line:
                        new_ad[k] = 1
                        break
        for word, flag in new_ad.items():
            if flag == 0:
                lines.append('> ' + word + '\n\n')
        with open(filename, 'w') as f:
            f.writelines(lines)

if __name__ == '__main__':
    init_ad()
    add_ad()
    delete_ad()




