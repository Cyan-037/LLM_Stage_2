'''
多进程开发必须写 __name__ == "__main__"
因为windows坑
- 因为windows需要区分主进程和子进程的代码

1. 导入进程工具包
    import multiprocessing
2. 通过进程类 实例化进程 对象
    子进程对象 = multiprocessing.Process()
3. 启动进程执行任务
    进程对象.start()
'''
import multiprocessing
import time


def eat():
    for _ in range(10):
        print('睡睡睡')
        time.sleep(1)

def sleep():
    for _ in range(10):
        print('吃吃吃')
        time.sleep(1)


if __name__ == '__main__':
    process_eat = multiprocessing.Process(
        group=None,         # group固定为None（python官方预留的参数，以后可能更新）
        target=eat,        # target目标,这个进程要执行什么代码，传入一个函数名, 注意不要带()
        name='吃',          # 给创建的这个进程起个名字
    )

    process_sleep = multiprocessing.Process(
        group=None,  # group固定为None（python官方预留的参数，以后可能更新）
        target=sleep,  # target目标,这个进程要执行什么代码，传入一个函数名, 注意不要带()
        name='睡😴',  # 给创建的这个进程起个名字
    )

    process_eat.start()     # 创建此进程开始工作
    process_sleep.start()   # 创建此进程开始工作