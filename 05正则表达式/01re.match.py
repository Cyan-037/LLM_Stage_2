'''
匹配字符串头部是否符合规则
'''

import re

# 调用re的基础方法，match search findall
'''
re.match 从被匹配的字符串的头部开始做匹配
如果匹配成功，则得到匹配结果
'''

# match 被匹配的字符串的头部是否符合规则
# 规则叫做itheima，被匹配的字符串的头部是否itheima
# 是 则匹配成功，匹配结果itheima
s = input('输入内容: ')

result = re.match(
    'itheima',  # 匹配规则（正则表达式本身）
    s,                  # 被匹配的字符串
)

# 获取结果
if result:              # 匹配成功result就是一个对象，失败就是none
    print('匹配成功')
    print('匹配结果：', result.group())
else:
    print('匹配失败')