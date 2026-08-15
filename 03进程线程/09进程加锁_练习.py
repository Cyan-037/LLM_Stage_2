'''
1. 有一个共享变量，存放int，默认值是100000
2. 有两个进程，分别对它10000次减一
3. 要求加锁，让最终结果是准确的80000
'''
import multiprocessing as mp

import time

def w1(v:mp.Value, lock:mp.Lock):
    for _ in range(10000):
        lock.acquire()
        v.value -= 1
        lock.release()

def w2(v:mp.Value, lock:mp.Lock):
    for _ in range(10000):
        lock.acquire()
        v.value -= 1
        lock.release()

if __name__ == "__main__":
    v = mp.Value('i', 100000)
    lock = mp.Lock()
    w1_p = mp.Process(target=w1, args=(v, lock))
    w2_p = mp.Process(target=w2, args=(v, lock))

    s = time.time()

    w1_p.start()
    w2_p.start()

    w1_p.join()
    w2_p.join()

    e = time.time()
    print(f'期望：80000')
    print(f'实际：{v.value}')
    print(f'耗时{e-s}s')