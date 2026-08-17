'''
进程1，每隔一秒生成一个随机数
    向队列添加put
进程2，得到进程1生成的随机数，判断是奇数还是偶数输出、
    从队列取出get

q.put() 从队尾放数据
q.get() 从队首拿数据
阻塞式，没数据一直等，等到有数据为止
q.get(block=False)  从队首取出数据，不阻塞，如果没数据就报错
q.qsize()   查看队列内部的数量
q.empty()   查看队列是否为空，为空返回True

队列的创建用multiprocessing库内提供的Queue，不用Python原生的，因为进程不安全
'''
import multiprocessing as mp
import time
import queue
import random

def w1(queue):
    for _ in range(100):
        num = random.randint(1, 1000)
        queue.put(num)
        print(f'w1放入：{num}')
        time.sleep(1)

def w2(queue):
    while True:
        # try:
        #     num = queue.get()
        # except Exception as e:
        #     continue
        num = queue.get()

        if num % 2 == 0:
            print(f'w2. 偶数：{num}')
        else:
            print(f'w2. 奇数:{num}')

if __name__ == '__main__':
    # q = queue.Queue()   # ❌ 线程安全队列，不能跨进程
    '''
    queue.Queue 是线程安全的，但不能用于进程间通信。
    在 multiprocessing 中必须使用 multiprocessing.Queue，否则数据无法在子进程间传递（会抛出异常或直接卡死）。
    '''
    q = mp.Queue()
    mp.Process(target=w1, args=(q,)).start()
    mp.Process(target=w2, args=(q,)).start()
