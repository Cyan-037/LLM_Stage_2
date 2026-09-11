import numpy as np

# 创建数组
arr = np.arange(1, 13)
print('原始数组：\n', arr)
print('维度', arr.ndim)
print('形状', arr.shape)

# 重塑
arr2 = arr.reshape((3,4))  # 传入元组(x,y)，x行y列
print('3*4后：\n', arr2)
print('转置：\n', arr2.T)

# 摊平  展开变成1维
arr_flat = arr2.flatten()
print('摊平：\n', arr_flat)

# 调整大小
arr_resized = np.resize(arr, (3,6))
print('调整大小：\n', arr_resized)
arr_resized = np.resize(arr, (3,5))
print('调整大小：\n', arr_resized)

