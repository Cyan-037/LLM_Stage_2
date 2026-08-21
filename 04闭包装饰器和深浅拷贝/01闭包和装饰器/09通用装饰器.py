import time


def time_calc(fn):
    def inner(*args,**kwargs):
        # *args ==>元组
        # **kwargs ==> 字典
        s = time.time()
        z = fn(*args,**kwargs)
        e = time.time()
        print(f'运行时间{e-s}')
        return z
    return inner

@time_calc
def loop_print(num):
    for i in range(1, num+1):
        print(i)

@time_calc
def say_hi(name,age,gender):
    print(f'我是{name},今年{age}岁，性别{gender}')

loop_print(3)
say_hi('张三',38,'男')