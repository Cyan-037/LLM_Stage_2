'''
背景：
电商系统中多个用户可能同时购买同一种商品。如果多个线程同时扣减库存，库存结果可能不准确。下面用简单代码模拟两个线程同时扣库存的场景。
题目：
编写程序模拟两个线程扣减库存，要求：

初始库存 stock = 10。(1分)
定义函数 buy(name, count)，表示某个用户购买 count 件商品。(3分)
使用互斥锁保护库存判断和扣减过程。(3分)
创建三个线程，分别模拟用户购买 3 件、4 件、5 件商品。(2分)
线程结束后打印剩余库存。(1分)
'''

import threading
import time

stock = 10

def buy(name, count):
    global stock
    for i in range(count):
        if stock <=0 :
            print(f'库存归零,用户{name}还剩{count-i}件商品没购买')
            return
        else:
            lock.acquire()
            stock -= 1
            print(f'用户{name}购买了第{i+1}/{count}件商品')
            lock.release()
            time.sleep(1)
    print(f'用户{name}已购买完毕')

lock = threading.Lock()
t1 = threading.Thread(target=buy,name='一号',args=('张三',5))
t2 = threading.Thread(target=buy,name='二号',args=('李四',4))
t3 = threading.Thread(target=buy,name='三号',args=('赵五',3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f'剩余库存: {stock}')