'''
TTL: Time To Live # 剩余存活时间

1. 线程：作为计时器
2. 其他线程读取计时器的值，超时自我了解
'''
import threading
import time

# time_counter = 0
#
# def timer():
#     global time_counter
#     while True:
#         time.sleep(1)
#         time_counter += 1

def work():
    start_time = time.time()
    while True:
        print('我爱工作')
        time.sleep(1)
        if time.time() - start_time > 5:
            break

# t1 = threading.Thread(target=timer).start()
t2 = threading.Thread(target=work).start()

