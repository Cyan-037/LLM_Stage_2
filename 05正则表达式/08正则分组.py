import re

# | 匹配左右任意一个表达式，或者 的意思
# ()
# 1.将内容作为整体
# 2.将内容作为一个分组
# \数字   引用分组的内存

def demo01():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com.cn
    s = input('输入内容：')
    p = r"^<(\w+)>.*</\1>"

    r = re.match(p,s)
    if r:
        print('成功')
        print(r.group())
        print(r.group(0))
        print('第一个括号: ',r.group(1))
        print('第二个括号: ',r.group(2))
        print('第三个括号: ',r.group(3))
    else:
        print('匹配失败')

def demo02():
    '''
    邮箱 abcd@qq.com
    邮箱运行： @之前4-20，@之后，qq.com或sina.com或163.com
    输入字符是：
    abcd@qq.com二级域名abcd域名qq.com
    '''
    s = input('输入：')
    p = r"^(\w{4,20})@(qq\.com|sina\.com|163\.com)\s二级域名\1\s域名\2$"

    r = re.match(p,s)
    if r:
        print('成功',r.group())
        print("二级域名：",r.group(1))
        print('域名:',r.group(2))
    else:
        print('匹配失败')

def demo06():
    '''
    江河汇手机号，替换为185****1234
    :return:
    '''
    s = input('手机号：')
    p = r"(\d{3})\d{4}(\d{4})"

    r = re.sub(p, r"\1****\2", s)
    print(f'替换后：{r}')

demo06()