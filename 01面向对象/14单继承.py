'''
没有父类时，默认放object
> class 类:
或者
> class 类(object):

有父类时：
class 类(放继承的父类):

'''

class Animal(object):
    color = '黄'

    def __init__(self):
        self.name = '名字'
        self.__nickname = '二狗子'

    def __eat_fish(self):
        print('偷偷的说，我喜欢吃鱼')

    def eat(self):
        print('吃东西')

    def sleep(self):
        print('睡觉')

class Dog(Animal):
    def work(self):
        print('看家护院')

class Cat(Animal):
    def work(self):
        print('被撸')

cat = Cat()
print(cat.color,cat.name)
cat.work()
cat.eat()