'''
魔法方法，在Python的类中，有一批特殊名字的方法，只要你写的方法名字和他们相同，就有对应的功能。

- `__init__`，构造魔术方法，类创建会自动调用且会接收参数
- `__del__`，析构魔术方法，类销毁会自动执行
- `__str__`，print打印类对象的输出
- `__lt__`，小于大于符号比较
- `__le__`，小于等于，大于等于符号比较
- `__eq__`，相等比较
'''
import time


class Cat(object):

    def __init__(self):
        print("哈基米被创建了")

    def __del__(self):
        print("哈基米被销毁了")

cat = Cat()

del cat # 主动销毁cat, 此时程序还没结束

time.sleep(3) # 时间暂停三秒，三秒后继续执行
