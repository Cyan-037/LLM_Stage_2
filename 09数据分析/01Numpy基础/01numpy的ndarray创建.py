'''
数据分析三剑客
- numpy，科学计算库，主要做数学计算
- pandas，数据分析库，主要做数据多清洗过滤，统计分组，查询计算等
- matplotlib， 可视化框架，主要针对数据产出可视化图表（衍生于MATLAB）

三者关系
- numpy提供底层数学计算支持
- pandas提供数据的处理，整理，分析，统计
- matplotlib，完成结果的可视化展示

不是python自带的，需要安装
'''
import numpy as np  # 惯性缩写为np

# numpy核心数据结构，ndarray

# 将pyhton的数据都转为ndarry才能用numpy进行处理
# 从列表创建数组
arr1 : np.ndarray = np.array([1, 3, 5, 7, 9])
print('一维数组arr1: ', arr1, type(arr1))

arr2 = np.array([[1,2,3],[4,5,6]])
print('二维数组arr2: ', arr2)

# 创建特殊数组
# 全是0的数组
zeros_arr = np.zeros((3,4))     # 传入元组，三行四列，二维
print('全0数组：\n', zeros_arr)
# 全1的数组
ones_arr = np.ones((5,6))       # 元组，5行6列，二维，全是一
print('全1数组：\n',ones_arr)

# 创建序列数组，包头不包尾
range_arr: np.ndarray = np.arange(0, 10, 2)
print('序列数组: \n', range_arr, type(range_arr))

# 等分数组
linspace_arr = np.linspace(0, 12, 6)
print('等分数组: \n', linspace_arr)

# 随机数组
random_arr = np.random.rand(3,3)
print('随机数组：\n', random_arr)

# 标准正态分布数组
randn_arr = np.random.randn(3,3)
print('随机数组：\n', randn_arr)

