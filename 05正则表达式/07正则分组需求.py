
import re

# | 匹配左右任意一个表达式，或者 的意思
# ()
# 1.将内容作为整体
# 2.将内容作为一个分组
# \数字   引用分组的内存

def demo01():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com.cn
    s = input('输入内容：')
    p = r"^(\w{4,20})@(163|qq|sina)\.(com|cn)$"

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

demo01()