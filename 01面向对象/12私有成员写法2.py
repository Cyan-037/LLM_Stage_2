'''

私有成员写法：
- 单下划线开头：程序员之间约定俗成,防君子不防小人，因为最早python没有这个功能
- 双下划线开头：语法上的限制，强制不给用，后来更新的

'''
class Student(object):
    def __init__(self, name):
        self.name = name
        self._balance = 1000 # 私有的意思，但没有语法保护