import re

'''
re.sub(规则, 要替换成的内容, 被替换字符串)
'''
def demo1():
    # 数字替换为*
    s = 'abc123def456'
    p = r'\d'

    result = re.sub(p, "*", s)
    print(result, type(result))


def demo2():
    # 非数字替换为-
    s = 'abc123def456'
    p = r'\D'

    result = re.sub(p, "-", s)
    print(result, type(result))

# 替换.为#
def demo3():
    # 把点替换为#，.代表任意值，\.转义字符加.代表.本身
    s = 'www.qq.com'
    p = r'\.'

    result = re.sub(p, "#", s)
    print(result, type(result))

# 指定替换的次数
def demo4():
    s = 'www.qq.com'
    p = r'\.'

    # 把点替换为#，只换前两个
    result = re.sub(p, "#", s, count=2)
    print(result, type(result))

demo1()
demo2()
demo3()
demo4()