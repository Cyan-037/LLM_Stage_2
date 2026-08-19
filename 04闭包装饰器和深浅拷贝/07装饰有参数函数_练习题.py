'''
1. 被修饰函数，接受3个参数传入，计算三个参数的和并print输出
2. 装饰器装饰函数，在函数执行前输出开始，执行后输出结束
'''

def add_v1(fn):
    def inner(x,y,z):
        print('装饰开始')
        fn(x,y,z)
        print('装饰结束')
    return inner

@add_v1
def add(x, y, z):
    print(f'x + y + z = {x + y + z}')

add(1,2,3)