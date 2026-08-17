'''
1. 开发2个线程，线程1，每隔一秒输出我在唱歌，输出十次
2. 线程2，每隔一秒输出我在吃饭，输出5次
'''
import threading
import time

def sing():
    for _ in range(10):
        print('我在唱歌')
        time.sleep(1)

def eat():
    for _ in range(5):
        print('我在吃饭')
        time.sleep(1)

# 多线程不需要写 if __name__ == '__main__':
# 写上也没有坏处
threading.Thread(target=sing, name='唱歌').start()
threading.Thread(target=eat, name='吃').start()