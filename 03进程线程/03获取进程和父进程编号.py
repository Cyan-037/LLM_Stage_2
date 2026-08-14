import multiprocessing as mp
import time

def eat(num):
    # 获取自己这个进程的进程对象
    eat_process = mp.current_process()
    # 获取自己进程的相关信息
    pid = eat_process.pid
    pname = eat_process.name
    print(f'子进程id:{pid},子进程名称:{pname}')

    # 获取父进程id
    import os
    pid = os.getpid()
    ppid = os.getppid()
    print(f'子进程id:{pid},父进程id:{ppid}')

    for i in range(1, num+1):
        print(f'我吃第{i}次')
        time.sleep(1)

def sleep(num, sec):
    # 获取自己这个进程的进程对象
    sleep_process = mp.current_process()
    # 获取自己进程的相关信息
    pid = sleep_process.pid
    pname = sleep_process.name
    print(f'子进程id:{pid},子进程名称:{pname}')

    for i in range(1, num+1):
        print(f'我睡觉第{i}次')
        time.sleep(sec)

if __name__ == '__main__':
    # current_process获取自己的进程对象
    main_process = mp.current_process()
    print(f'主进程id:{main_process.pid},主进程名称:{main_process.name}')

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