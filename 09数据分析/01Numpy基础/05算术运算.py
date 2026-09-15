import numpy as np

a = 10
b = 5
# 幂运算
print('幂运算：', a ** b)

# 矩阵乘法      点积和模长是计算余弦相似度的基础算术运算
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
res = np.dot(arr1,arr2)
print(res)
