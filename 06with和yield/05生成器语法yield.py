'''
生成器函数搭配yield：
    当推导式语法，不足以描述你想要的数据生成规则，就需要写函数搭配yield
    只要函数中有yield，那就是生成器，yield返回一个数据，yield可以重复使用,不会直接结束函数，用了yield就不要用return了
'''

# 得到1个1-10级数的生成器，要求写def和yield
def num_gen():
    print('啦啦啦')
    print('咔咔咔')
    yield 1         # yield对外生成一条数据，生成后代码暂停，直到对方需要下一个数据代码继续向下
    print('咔咔咔')
    yield 3
    print('咔咔咔')
    yield 5
    print('咔咔咔')
    yield 7
    print('咔咔咔')
    yield 9

gen = num_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
