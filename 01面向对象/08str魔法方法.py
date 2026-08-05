'''
直接打印stu或者强转str都只会打印内存地址

__str__:
当类对象被转为字符串时，应当返回什么结果
即这个方法，在类对象被转换为字符串的时候，自动被调用

'''
class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我叫{self.name},今年{self.age}岁"

stu = Student('张三',32)

print(stu)