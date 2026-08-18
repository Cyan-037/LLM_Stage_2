'''
2 线程，线程1对共享变量num+=1 +10000
线程2同样num+=1 +10000
num起始是0
'''
import threading

num = [0]
num1 = 0


def w1():
    for _ in range(10000):
        num[0] += 1

        global num1
        num1 += 1

        print(num)
        print(num1)


def w2():
    for _ in range(10000):
        num[0] += 1

        global num1
        num1 += 1

        print(num)
        print(num1)


threading.Thread(target=w1).start()
threading.Thread(target=w2).start()
