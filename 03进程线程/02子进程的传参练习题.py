'''
1. 2个子进程，一个子进程，接收一个数字传入，每隔1秒输出数字，输出的数字是1,2,3.。到传入的数字结束
2. 子进程2，同样接受一个数字，也是输出1,2,3到传入的数字结束，同时也接受一个name，要求输出数字+name
'''
import multiprocessing as mp
import time

def number1(num):
    for i in range(num):
        print(i+1)
        time.sleep(1)

def number2(num, name):
    for i in range(num):
        print(f"{i+1}   {name}")
        time.sleep(1)

if __name__ == '__main__':
    prcs1 = mp.Process(target=number1,args=(10,))
    prcs2 = mp.Process(target=number2, args=(10,'茱莉亚'))

    prcs1.start()
    prcs2.start()
