'''
写一个函数搭配yield得到生成器
生成的规则是，随机提供10个数字（范围1-100）
'''
import random

def gen():
    for _ in range(10):
        i = random.randint(1,100)
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))