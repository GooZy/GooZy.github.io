# -*- coding: utf-8 -*-
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
import glob

ad = [
    '*VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>',
    '*VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>'
]

new_ad = {
    '*VPN*: <a href="https://portal.shadowsocks.la/aff.php?aff=11951" target="_blank">![shadowsocks](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/shadowsocks.png?raw=true)</a>': 0,
    '*QQ自助代刷*: <a href="http://qqzzds.hxcvb.com/" target="_blank">![qqzzds](https://github.com/GooZy/GooZy.github.io/blob/hexo/source/images/qqzzds.png?raw=true)</a>': 0,
}

def replace_ad():
    for filename in glob.glob('*.md'):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                for i in range(0, len(ad), 2):
                    if ad[i] in line:
                        lines[index] = line.replace(ad[i], ad[i + 1])
        with open(filename, 'w') as f:
            f.writelines(lines)

            
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
    #replace_ad()
    init_ad()
    add_ad()