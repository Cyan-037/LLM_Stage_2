'''
多态,多用在继承关系上，因为有父类定义声明兜底，子类都包含父类的成员方法，不会出现传入参数不包含该功能的情况，导致报错
>以父类作定义声明
>以子类做实际工作
>用以获得同一行为不同状态
'''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

# 子类一定大于等于父类，所以这里放父类，子类中一定包含相应的功能
def make_noise(animal: Animal):
    animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()

# 同一函数下的多种状态，多态
make_noise(animal)
make_noise(dog)
make_noise(cat)