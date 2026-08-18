'''
写一个线程，无限循环每隔一秒输出信息（内容随意），要求：主线程内无限循环得到随机数，如果随机数是5，则停止线程
'''
import threading
import random
import time

flag = True

def w1():
    global rd
    while True:
        if not flag:
            print('随机数5退出循环')
            break
        print('嘟嘟哒嘟嘟')
        time.sleep(1)


if __name__ == '__main__':

    threading.Thread(target=w1).start()
    while True:
        rd = random.randint(1,100)
        # print(rd)
        if rd == 5:
            flag = False
            break
        time.sleep(0.1)
