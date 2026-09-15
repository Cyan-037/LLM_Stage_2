import numpy as np

# 广播示例
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = np.array([10,20,30])

print('数组a：\n', a)
print('数组b：\n', b)
print('广播加法：\n', a+b)   # b被广播到a的每一行

c = np.array([[1],[2],[3]]) # 3*1   每一行，广播给对方的每一行，1给了a里面的[1,2,3]，2给了a里面的[4,5,6]
print('广播乘法：\n', a * c)
