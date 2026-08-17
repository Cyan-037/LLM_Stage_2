import multiprocessing as mp
import time

def eat(num):
    for i in range(1, num+1):
        print(f'我吃第{i}次')
        time.sleep(1)

def sleep(num, sec):
    for i in range(1, num+1):
        print(f'我睡觉第{i}次')
        time.sleep(sec)

if __name__ == '__main__':
    eat_process = mp.Process(
        target=eat,
        args=(10,)   #元组，按顺序传参给函数
    )

    sleep_process = mp.Process(
        target=sleep,
        args=(10,4)   #
    )


    eat_process.start()
    sleep_process.start()