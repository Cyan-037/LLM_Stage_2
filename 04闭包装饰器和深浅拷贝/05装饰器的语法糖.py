'''
Python提供了语法糖装饰器

@改进函数名
原函数

功能：直接将原函数替换为改进函数的内部函数，不需要再声明(相同效果)
say_hi = buff(say_hi)

'''
def buff(fn):
    def inner():
        print('我干活了')
        fn()
    return inner

# 语法糖
@buff
def say_hi():
    print('你好')

say_hi()