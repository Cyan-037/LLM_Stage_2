class Dog(object):

    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f'这只狗叫{self.name},颜色是{self.color},已经{self.age}岁了'

dog1 = Dog('大黄','黄色',2)
print(dog1)