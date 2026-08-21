'''
1. 被修饰函数，接受3个参数传入，计算三个参数最大的数字并return
2. 装饰器装饰函数，在函数执行前输出开始，执行后输出结束
'''

def max_v1(fn):
    def inner(x,y,z):
        print('装饰开始')
        ans = fn(x,y,z)
        print('装饰结束')
        return ans
    return inner

@max_v1
def max_three(x, y, z):
    a = max(x,y,z)
    return a

print(max_three(1,2,3))