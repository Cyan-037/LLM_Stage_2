import numpy as np
'''
1. 创建一个二维，内容不限，结构3*4
2. 取出 第二行第三列
3. 取出第二行第三行，第二第三列
4. 创建1个1维数组内容不限，元素数量15个
5. 将其重塑为3*5的二维
6. 转换为5*3的二维
7. 将5*3的二维摊平得到1维
'''
arr = np.arange(1,13)
arr = arr.reshape((3,4))
print('第一个：\n', arr)

print('第二行第三列：\n', arr[1,2])
print('第二行：\n', arr[1])
print('第三行：\n', arr[2])
print('第二列：\n', arr[:, 1])
print('第三列：\n', arr[:, 2])

arr1 = np.arange(1,16)
print('arr1: \n',arr1)
arr1 = arr1.reshape((3,5))
print('arr1: \n',arr1)
arr1_T = arr1.T
print('arr1_T: \n',arr1_T)
arr2 = arr1_T.flatten()
print('arr2: \n',arr2)
