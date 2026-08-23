import re

def print_result(result):
    if result:              # 匹配成功result就是一个对象，失败就是none
        print('匹配成功')
        print('匹配结果：', result.group())
    else:
        print('匹配失败')

def demo01():
    '''
    匹配字符串是否是：
    - 开头有三个字符，内容随意
    - 结尾有三个字符，内容随意
    - 中间必须是itheima
    :return:
    '''
    # 正则中 . 代表字符数量1，内容随意（\n除外）
    s = input('输入内容：')
    result = re.match(
        '...itheima...',    # 规则,前面三个随意字符，后面三个随意字符，中间必须是itheima
        s
    )
    print_result(result)

def demo02():
    '''
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
    [ab]  表示1个字符，内容非a即b
    [abcde]  表示1个字符，内容a或b或c或d或e
    第一个字符是小写字母：[abcdefghijklmnopqrstuvwxyz]
    abcdefghijklmnopqrstuvwxyz
    :return:
    '''
    s = input('输入内容：')
    result = re.match(
        "[abcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZ][0123456789]",  # 规则,前面三个随意字符，后面三个随意字符，中间必须是itheima
        s
    )
    print_result(result)

def demo03():
    '''
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
    [ab]  表示1个字符，内容非a即b
    [abcde]  表示1个字符，内容a或b或c或d或e
    第一个字符是小写字母：[abcdefghijklmnopqrstuvwxyz]
    abcdefghijklmnopqrstuvwxyz
    :return:
    '''
    s = input('输入内容：')
    result = re.match(
        "[a-z][A-Z][0-9]",  # 规则,前面三个随意字符，后面三个随意字符，中间必须是itheima
        s
    )
    print_result(result)

def demo04():
    '''
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母或大写字母
    '''
    s = input('输入内容：')
    result = re.match(
        "[a-zA-Z]",
        s
    )
    print_result(result)

def demo05():
    '''
    字符串必须符合规则：
    - 从头开始，第一个字符是除了小写字母和大写字母之外的任何字符
    '''
    s = input('输入内容：')
    result = re.match(
        "[^a-zA-Z]",
        s
    )
    print_result(result)

def demo06():
    '''
    三个任意数字
    '''
    s = input('输入内容：')
    result = re.match(
        " \d\d\d",
        s
    )
    print_result(result)

demo06()