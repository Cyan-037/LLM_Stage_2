'''
python 用不了多核cpu，用不了并行
python抢资源的方法只有多进程

Python多线程可以实现多个任务并发执行，减少不必要的等待

# 多线程库
import threading

# 和 multiprocessing.Process(target=.., name=..)一样布局
threading.Thread(target=.., name=..)
'''
import time
import threading

def eat():
    print('吃')
    time.sleep(3)
    print('吃完了')

def sleep():
    print('要睡了')
    time.sleep(7)
    print('睡爽了')

if __name__ == '__main__':
    thread_eat = threading.Thread(target=eat, name='吃货线程')
    thread_sleep = threading.Thread(target=sleep, name='睡神线程')

    # 多进程：eat和sleep是可以并行的（多个核心同时跑）
    # 多线程：Python中1个进程不管多少线程，只能用一个核心，所以eat和sleep是并发执行（交替）
    thread_eat.start()
    thread_sleep.start()