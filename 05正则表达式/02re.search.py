'''
找到从左到右第一个符合规则的
'''

import re

def print_info(result):
    if result:
        print('匹配成功')
        print('匹配结果为: ',result.group())

def demo0():
    s = input('输入内容：')
    p = r"\d\d\d"

    result = re.search(p, s)
    print_info(result)

def demo1():
    s = input('输入内容：')
    p = r"#..#"

    result = re.search(p, s)
    print_info(result)

demo1()