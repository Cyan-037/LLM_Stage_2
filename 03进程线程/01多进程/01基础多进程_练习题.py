'''
开发两个进程，一个进程无限循环输出我爱学习，每隔一秒输出一次
另一个进程每隔一秒输出我要吃饭
注意，创建进程和启动进程的代码，写在if __name__ == '__main__':里面才行
'''

import multiprocessing as mp
import time


def study():
    while True:
        print('我爱学习')
        time.sleep(1)

def eat():
    while True:
        print('我要吃饭')
        time.sleep(1)


if __name__ == '__main__':
    process_study = mp.Process(target=study, name='学习进程')

    process_eat = mp.Process(target=eat, name='吃饭进程')

    process_study.start()
    process_eat.start()