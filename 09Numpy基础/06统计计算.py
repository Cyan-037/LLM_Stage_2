import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('数组:\n', arr)

print('总和：\n', np.sum(arr))
print('每列总和：\n', np.sum(arr,axis=0))    # 0表示列方向
print('每行总合: \n', np.sum(arr, axis=1))   # 1表示行方向

print('平均值：\n',np.mean(arr))        # mean平均
print('标准差: \n', np.std(arr))
print('方差：\n', np.var(arr))

print("最大：\n", np.max(arr))       # 最大值
print('最大值的索引:\n', np.argmax(arr))