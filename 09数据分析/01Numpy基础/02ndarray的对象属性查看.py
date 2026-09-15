import numpy as np

# 创建示例数组
arr: np.ndarray = np.array([[1,2,3],[4,5,6]])

# 属性，ndarray是一个class的类对象，类里面有方法也有变量（属性）
print('数组：', arr)
print('数组维度：', arr.ndim)    # 访问ndim成员属性
print('数组形状：', arr.shape)   # 形状（行数，列数）
print('数组大小：', arr.size)    # 元素总数
print('数据类型：', arr.dtype)   # 存档数据类型
# 数组int默认存储为int64（8个字节）
# python的int默认存储为int32（32个二进制，8个二进制一个字节，共4个字节）

# 练习 创建一个ndarray对象，要求输出维度数量和几行几列
a : np.ndarray = np.array([[3,4,65,7],[3,5,7,89]])
print('数组本身：\n', a)
print('维度：', a.ndim)
print('数量：', a.size)
print('形状：', a.shape)