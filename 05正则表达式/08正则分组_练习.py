'''
1. 经手机号替换为1*********1 中间九个数字为*
2. 微博超话 #.....#，抽取2个#的内容输出
3. IP地址xxx.xxx.xxx.xxx  输出中间第二个和第三个xxx，分开输出
4. 网址：http://www.qq.com, 分别输出
    协议，即http或https
    域名，即qq.com
    协议http或https
    域名支持qq.com，sina.com itheima.com itcast.cn
'''
import re


def demo01():
    s = '19820384934'
    p = r'^(\w)\w{9}(\w)$'
    result = re.search(p, s)
    if result:
        print('匹配成功')
        result = re.sub(p,r'\1*********\2', s)
        print('替换为:', result)

def demo02():
    s = "今日热点#周杰伦新歌#哈哈哈"
    p = r'#(\w+)#'
    r = re.search(p,s)
    print(r.group(1))
