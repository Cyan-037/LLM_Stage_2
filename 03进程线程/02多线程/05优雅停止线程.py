'''
Python 没有提供线程的terminate()方法
一般通过标志位完成

通过共享变量，标志位flag停止
'''
import time
import threading

flag = True

def work():
    while flag:
        print('我爱工作，工作使我强大')
        time.sleep(1)

t1 = threading.Thread(target=work)
t1.start()

time.sleep(5)
print('公司黄了，别干活了')

flag = False