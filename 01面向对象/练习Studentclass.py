'''
Student_class

'''
class Student(object):
    school_name = '黑马'

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu_1 = Student('张三',23)
stu_2 = Student('李四',22)

print(stu_1.name, stu_1.age, stu_1.school_name)
print(stu_2.name, stu_2.age, stu_2.school_name)

Student.school_name = '白马'

print(stu_1.name, stu_1.age, stu_1.school_name)
print(stu_2.name, stu_2.age, stu_2.school_name)
