'''
类：
类的属性，即定义在类中的变量（数据）
类的行为，即定义在类中的函数（方法）

设计一个类（图纸），基于类（图纸）创建对象（具体牛马），使用对象（具体牛马）的属性和行为，是对象在干活
'''

# 1. 设计一个表
class Student:
    name = None
    age = None
    adrs = None

    def say_hi(self):
        print(f'大家好，我叫{self.name},今年{self.age}岁,我家在{self.adrs}')

# 2. 打印具体的表
stu1 = Student()
stu2 = Student()

# 3. 让用户填数据（具体数据）
stu1.name = '张三'
stu1.age = 23
stu1.adrs = '张家村01号'

stu2.name = '李四'
stu2.age = 34
stu2.adrs = '李家村02号'

# 验证得到的信息
print(f'stu1 名字是{stu1.name}')
stu1.say_hi()