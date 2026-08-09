'''
静态方法
不需要建实例就可以用类名调用
不需要self也不需要cls就能建
需要@staticmethod

作用：让使用者知道这个方法和类有关
'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'大家好真的狗{self.name}, 今年{self.age}岁')

    @staticmethod
    def eat():
        print('吃')

# 不需要类属性或成员属性，但是又跟这个类有关，不需要建实例就可以用类名调用
Dog.eat()

# 静态的调用，可以用类名调用