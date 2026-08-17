'''
创建锁
mp.Lock()
一把锁，只有拿锁的进程才能用
'''

import multiprocessing as mp
from multiprocessing.synchronize import Lock
import time


def w1(v: mp.Value, lock: Lock):
    for _ in range(100000):
        lock.acquire()  # 上锁
        v.value += 1
        lock.release()  # 解锁


def w2(v: mp.Value, lock: Lock):
    for _ in range(100000):
        lock.acquire()  # 上锁
        v.value += 1
        lock.release()  # 解锁


if __name__ == '__main__':
    v = mp.Value('i', 0)
    lock = mp.Lock()

    w1_process = mp.Process(target=w1, args=(v, lock))
    w2_process = mp.Process(target=w2, args=(v, lock))

    s = time.time()
    w1_process.start()
    w2_process.start()

    w1_process.join()
    w2_process.join()

    e = time.time()
    print(f'期望:200000')
    print(f'实际:{v.value}')
    print(f'耗时:{e - s}s')