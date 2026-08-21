'''
如果列表没有嵌套列表，直接浅拷贝无法全部区分
在嵌套区域两者又混在一起了
用深拷贝copy.deepcopy()
'''
from copy import deepcopy

lst1 = [1,2,['a','b','c']]
lst2 = lst1.copy()
lst3 = deepcopy(lst1)

print(lst1)
print(lst2)
print(lst3)
print('===================')

lst1.append(3)
print(lst1)
print(lst2)
print(lst3)
print('===================')

lst2[2].append('d')
print(lst1)
print(lst2)
print(lst3)