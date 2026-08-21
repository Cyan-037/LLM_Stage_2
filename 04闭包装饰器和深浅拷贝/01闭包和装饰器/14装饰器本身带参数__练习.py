'''
准备一个被修饰的函数，内容随意
准备一个装饰器，装饰器接收一个name参数
在被修饰的函数执行之后，print输出这个name
'''


def outer(name):
    def middle(fn):
        def inner():
            fn()
            print(f'你的名字是{name}')
        return inner
    return middle

@outer('张三')
def hi():
    print('我是谁')

hi()