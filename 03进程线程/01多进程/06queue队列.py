import queue

# 创建队列对象
q = queue.Queue(10)     # 参数表示最多容纳多少元素，如果不填，基本无限(看内存)

# 放入数据，尾部入列
q.put(1)

# 取出数据
num = q.get()
print(num)

# 判断队列大小
print(q.qsize())