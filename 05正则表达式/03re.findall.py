import re

'''
re.match    从头匹配            ==> result.group()
re.search   全串搜索，返回第一个  ==> result.group()
re.findall  全串搜索，得到全部   ==>  result:list
'''

s = input('输入: ')
p = r"#..#"

result: list = re.findall(p, s)
print(result)