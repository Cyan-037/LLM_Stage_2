g_list = []

# 模拟放入队列
for i in range(1, 11):
    g_list.append(i)    # 追加（尾部放入）

for _ in range(1, 11):
    num = g_list.pop(0) # pop按照下标删除元素，并返回元素值
    print(num)
print(f'list还剩余：{len(g_list)}')