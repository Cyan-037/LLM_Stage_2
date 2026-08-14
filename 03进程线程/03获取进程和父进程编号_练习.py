'''
1. 创建2个子进程，内容随意
2. 在子进程1和2通过multiprocessing模块打印子进程1的pid和name
3. 在主进程代码中，用os模块获取pid和ppid并print出来
'''
import multiprocessing as mp
import time
import os

def p1(num):
    cp = mp.current_process()
    print(f'当前子进程pid:{cp.pid}, 当前子进程名字:{cp.name}')

    for _ in range(num):
        print('这是进程1')
        time.sleep(1)

def p2(num,name):
    cp = mp.current_process()
    print(f'当前子进程pid:{cp.pid}, 当前子进程名字:{cp.name}')
    
    for _ in range(num):
        print(f'这是进程2,{name}')
        time.sleep(1)

if __name__ == '__main__':
    main_pid = os.getpid()
    main_ppid = os.getppid()
    print(f'当前进程id是：{main_pid}, 父进程id是:{main_ppid}')

    prc1 = mp.Process(target=p1, args=(10,))
    prc2 = mp.Process(target=p2, args=(10,'张三'))

    prc1.start()
    prc2.start()