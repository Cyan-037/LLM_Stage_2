# 装饰其他函数，其他函数内容随意
# 装饰器功能是：
#     执行先输出“我来了”在执行被装饰函数
#     最后再输出“结束了”
def buff(f):
    def inner():
        print('我来了')
        f()
        print('结束了')

    return inner


@buff
def hello():
    print('你好')


hello()
