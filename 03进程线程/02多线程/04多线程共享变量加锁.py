'''
线程锁
threading.Lock
'''
import threading

num = [0]
num1 = 0
lock = threading.Lock()

def w1(lock):
    for _ in range(10000):
        lock.acquire()
        num[0] += 1

        global num1
        num1 += 1

        print(num)
        print(num1)
        lock.release()


def w2(lock):
    for _ in range(10000):
        lock.acquire()
        num[0] += 1

        global num1
        num1 += 1

        print(num)
        print(num1)
        lock.release()


threading.Thread(target=w1, args=(lock,)).start()
threading.Thread(target=w2, args=(lock,)).start()
