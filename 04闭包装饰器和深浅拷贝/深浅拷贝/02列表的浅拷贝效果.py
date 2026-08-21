'''
浅拷贝，让b列表赋值给a列表，然后两个列表各自独立，互不影响，不要用=，而是用copy（）方法
'''

lst1 = [1,2,3]
lst2 = lst1.copy()

print(lst1)
print(lst2)

lst2.append(4)

print(lst1)
print(lst2)