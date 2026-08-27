'''
一个类只要实现了__enter__()和__exit__()两个方法，通过该类创建的对象我们就称之为上下文管理器
上下文管理器可以使用with语句
    with语句之所以这么强大，背后就是有上下文管理器做支撑的

实现上下文管理器：
    实现__enter__()和__exit__()，通过with进行管理

'''
import time


class MyClass:
    def __enter__(self):
        '''enter 进入'''
        print('我进来了')

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''exit退出'''
        print('我退出了')


with MyClass() as mc:
    print(mc)
    time.sleep(5)