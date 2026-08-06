'''

设计一个person类，内含name，age两个成员属性，内含work，sleep两个方法，内容随意
设计一个student类继承person类
给student提供自己的方法

'''
import time
class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def work(self):
        print('工作中')
        time.sleep(0.5)
        print('工作结束')

    def sleep(self):
        print('睡觉中')
        time.sleep(0.5)
        print('睡醒了')

class Student(Person):
    def goto_school(self):
        print('去上学')
    def do_homework(self):
        print('做作业')

小明 = Student('小明',12)
小明.goto_school()
小明.work()
小明.sleep()
小明.do_homework()