# 通用装饰器
def buff(fn):
    def inner(*args,**kwargs):
        print('开始')
        z = fn(*args,**kwargs)
        print('结束')
        return z
    return inner

@buff
def loop_print(num):
    for i in range(1, num+1):
        print(i)

@buff
def say_hi(name,age,gender):
    print(f'我是{name},今年{age}岁，性别{gender}')

loop_print(3)
say_hi('张三',38,'男')