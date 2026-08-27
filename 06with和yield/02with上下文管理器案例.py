'''
需求：写一个class类，类提供一个random_line()方法，调用向文件内追加随机内容
'''

import random
import time


class MyClass(object):

    def __init__(self, path):
        self.f = open(path, 'a', encoding='UTF-8')

    def __enter__(self):    # with开始执行会自动调用
        print('即将开始工作')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # with执行完毕会自动调用，里面是python自动传入的变量，即使报异常退出也会自动执行
        print('退出，关闭文件')
        self.f.flush()
        self.f.close()

    def random_line(self):
        lines = [
            '你好',
            '今天很开心',
            '祝你幸福',
            '嘟嘟哒嘟嘟'
        ]
        self.f.write(random.choice(lines))
        self.f.write('\n')

# 写法1
mc = MyClass('data.txt')
with mc:
    for _ in range(5):
        mc.random_line()
        time.sleep(1)

# (推荐)写法2: 想用写法2需要__enter__()加一个return self，返回自身
with MyClass('data.txt') as q:
    for _ in range(5):
        q.random_line()
        time.sleep(1)
