'''
import ..
g_list = []

def ..
def ..

if __name__ == "__main__"

三个进程（主进程，子进程1，子进程2）各自一份g_list变量，互相内存不共享

如果想让两个进程共享一个单值变量，如下所示
'''
import multiprocessing as mp
import time

def work1(num):
    for i in range(10):
        # .value 是访问共享数据的唯一入口
        num.value += 1
        print('w1',num.value)
        time.sleep(1)

def work2(num):
    for i in range(10):
        # # .value 是访问共享数据的唯一入口
        print('w2',num.value)
        time.sleep(1)

if __name__ == '__main__':
    value = mp.Value(
        'i',    # 类型 i-int, f-float, d-double, b-bool
        0       # 初始值
    )
    wk1_p = mp.Process(target=work1, args=(value,))
    wk2_p = mp.Process(target=work2, args=(value,))

    wk1_p.start()
    wk2_p.start()