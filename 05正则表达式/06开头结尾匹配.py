import re
'''
^表示字符串开头
$表示字符串结尾含义
r"^1\d{10}$"
'''

def demo01():
    """匹配手机号，必须1开头，其余数字11位"""
    s = input('输入：')
    # 10位
    p = r"^1\d{10}$"
    # match其实不用^，因为match就是从开头匹配
    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print('匹配失败')

def demo02():
    '''匹配密码，必须6位纯数字'''
    s = input('输入：')
    p = r"^\d{6}"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print('匹配失败')

