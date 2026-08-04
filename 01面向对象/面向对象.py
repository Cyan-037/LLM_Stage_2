'''
完整语法
class 类名称():
    类属性
    类属性

    def 成员方法(self):
        成员属性
        成员属性

        方法体代码

    def 类方法（）：
        方法体代码

属性和方法
分为：
1. 类属性，成员属性
2. 类方法，成员方法
'''
class Dog(object):
    # 类属性，也叫公有属性
    color = '黄'
    # 1. __init__ 在创建类对象的时候自动调用
    # 2. 在创建类对象的时候传入的参数，会自动传给__init__
    def __init__(self, name, food, age):
        # 成员属性，也叫私有属性，属于每个类对象本身self
        self.name = name
        self.food = food     # self代表类对象本身,代表从外部传入的参数给到self本身
        self.age = age

dog1 = Dog('大黄','米饭',3)
dog2 = Dog('小黑','披萨',2)
print(f"{dog1.name}的颜色是{dog1.color}色，它吃{dog1.food}，今年已经{dog1.age}岁了")

# 成员属性的修改
dog1.food = '酸奶'
print(dog1.food)


print(dog1.color, dog2.color)
# 类属性的修改
# 修改类属性color
Dog.color = '黑'
print(dog1.color, dog2.color)

# 此时相当于给dog1加了一个新的成员属性color，然后修改，只跟dog1有关，dog1.color访问的就是这个成员属性而不是类属性
# 由于dog2没有成员属性color，所以访问的就是类属性
dog1.color = '白'
print(dog1.color, dog2.color)

# dog1不会随其他的变棕
Dog.color = '棕'
print(dog1.color, dog2.color)