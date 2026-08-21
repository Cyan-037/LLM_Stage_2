'''
装饰器1,2,3，分别输出开始1,2,3
'''
def buff1(fn):
    def inner(*args,**kwargs):
        print('1开')
        fn(*args,**kwargs)
        print('1关')
    return inner

def buff2(fn):
    def inner(*args,**kwargs):
        print('2开')
        fn(*args,**kwargs)
        print('2关')
    return inner

def buff3(fn):
    def inner(*args,**kwargs):
        print('3开')
        fn(*args,**kwargs)
        print('3关')
    return inner

@buff1
@buff2
@buff3
def say_hi(name,age,gender):
    print(f'我是{name},今年{age}岁，性别{gender}')

say_hi('张三',38,'男')
