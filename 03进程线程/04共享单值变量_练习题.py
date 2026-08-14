'''
1. 创建一个Value类对象在2个进程之间共享
2. 进程1每隔两秒，将共享的Value-1
3. 进程2每隔两秒，print共享的value
4. value初始值为100
'''
import multiprocessing as mp
import time

def decay(num):
    while True:
        time.sleep(2)
        num.value -= 1
        if num.value == 0:
            break

def print_value(num):
    while True:
        time.sleep(2)
        print(num.value)
        if num.value == 0:
            break

if __name__ == '__main__':
    value = mp.Value('i', 100)
    mp.Process(target=decay, args=(value,)).start()
    mp.Process(target=print_value, args=(value,)).start()

