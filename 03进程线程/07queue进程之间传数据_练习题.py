'''
1. 隔一秒放一个数据
2.从队列取出，乘十print
'''
import multiprocessing as mp
import time
import random

def w1(num: mp.Queue):
    for _ in range(100):
        num.put(random.randint(1,1000))
        time.sleep(1)

def w2(num: mp.Queue):
    while True:
        value = num.get()
        print(value*10)

if __name__ == '__main__':
    q = mp.Queue()
    mp.Process(target=w1, args=(q,)).start()
    mp.Process(target=w2, args=(q,)).start()
