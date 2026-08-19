'''
写一个装饰器，被装饰的函数能够输出执行时间（秒）
'''
import time

def show_time(f):
    def inner():
        s = time.time()
        f()
        e = time.time()
        print(f'{e - s}')
    return inner

@show_time
def compute1():
    for _ in range(200000):
        1 + 1

@show_time
def compute2():
    for _ in range(2000):
        for _ in range(2000):
            1 + 1

compute1()
compute2()

