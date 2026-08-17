'''
当进程对象，调用join()后，则代码会阻塞在这里，只有子进程执行完毕才会下一步
'''

import multiprocessing as mp
import time
import random

def w1(num: mp.Queue):
    for _ in range(3):
        num.put(random.randint(1,1000))
        time.sleep(1)

def w2(num: mp.Queue):
    for _ in range(3):
        value = num.get()
        time.sleep(2)
        print(value*10)

if __name__ == '__main__':
    q = mp.Queue()
    w1_process = mp.Process(target=w1, args=(q,))
    w2_process = mp.Process(target=w2, args=(q,))

    w1_process.start()
    w2_process.start()

    # 必须2个子进程执行完成，才执行下面的代码
    w1_process.join()   # 卡住，直到w1子进程执行结束
    print('w1结束')
    w2_process.join()   # 卡住，直到w2子进程执行结束
    print('w2结束')

    print('主进程没代码了')