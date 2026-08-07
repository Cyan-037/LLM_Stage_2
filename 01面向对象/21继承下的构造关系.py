'''
子类没有init,父类有init，创建实例时提供的传递到父类


MRO (method resolution order)
在继承下，子类可以查看其MRO，MRO标示了：
子类对象使用成员的时候的查找顺序
子类在被实例化（创建对象）的时候，按照mro顺序，挨个实例化

MRO是一个内置元组，可以通过类名.__mro__获得

'''
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Dog(Animal):
    pass

dog = Dog('大黄','黄色')

print(Dog.__mro__)
