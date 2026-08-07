'''
父类有init，子类也有init

此时传入参数都被子类的init的截流，父类收不到，要手动调用父类init进行传参
'''
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self,name, color, age):
        self.age = age
        super().__init__(name, color)

dog = Dog('大黄','黄色',1)

print(dog.name)
print(dog.color)
print(dog.age)