'''
例如:
手机 + nfc + 红外遥控器 = 小米手机
class 类名（父类1，父类2，父类3）：

练习：
设计一个Animal类提供一个eat方法
设计一个worker类提供work方法
设计一个Student类提供study方法
设计一个Me类，集成上面三个类，类的内容是pass

pass 关键词用在设计一个类，一个函数的时候，仅需要起基础结构，不提供代码，就可以用pass代替
因为不用pass有语法错误，所以写pass
'''

class Animal(object):
    def eat(self):
        print('吃饭')

class Worker(object):
    def work(self):
        print('工作')

class Student(object):
    def study(self):
        print('学习')

class Me(Animal, Worker, Student):
    pass

me = Me()
me.eat()
me.work()
me.study()