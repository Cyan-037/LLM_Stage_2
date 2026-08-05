'''
提供一个lt,能进行大小比较
__lt__  __gt__  __le__  __ge__  __eq__  __ne__
less than
greater than
less equal
greater equal
equal
not equal
'''


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        '''self是比较大发起者，other被比较的另一个，比较小于'''
        # 当类对象使用 < 符号和他人比较，会自动查找__lt__方法执行做比较，被比较的other会自动传入此方法
        print('要比较小于了', self, other)
        return self.age < other.age


stu1 = Student('张三', 32)
stu2 = Student('李四', 22)

if stu1 < stu2:
    print('stu2是哥哥')
else:
    print('stu1是哥哥')
