import numpy as np

# 创建数组
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print('原始数组：\n', arr)
print('维度：\n', arr.ndim)

# 索引和切片
print('第一个：', arr[0][0])
print('最后一行：', arr[-1])
print('第二列：', arr[:, 1])    # arr[行,列]，冒号表示该维度上取全部索引，arr[:,1]代表全部索引行的第二列，也就是第二列整体
print('前两行前两列：', arr[0:2, 0:2]) # 切片，a:b左闭右开，0:2 包含0不包含2

print('前两行的2,3列\n', arr[0:2, 1:3])
print('前三行的234列\n', arr[:, 1:])

# 布尔索引
bool_arr = arr > 5
print('布尔结果：\n', bool_arr)
# 结果
# [[False False False False]
#  [False  True  True  True]
# [True True True True]]