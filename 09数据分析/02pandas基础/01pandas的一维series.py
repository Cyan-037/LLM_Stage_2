import pandas as pd
import numpy as np
'''
numpy纯玩数字，无法处理字符串
pandas是玩的是数据，可以处理字符串

pandas 两个核心数据结构： series一维带标签数组，dataframe二维

一维理解为只有一个列的数据库表
二维可以看作是有多个列的数据库表
'''
# series：一维带标签数组
# 从列表创建
s1 = pd.Series(["a","b","c"])
print(s1)
print(type(s1))
print("-"*40)

# 从字典创建
# 字典key作为数据的索引，字典的value就是数据
s2 = pd.Series({"a":1, "b": 2, "c": 3})
print(s2)

# 指定索引
s3 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s3)

# 取值
print('s3全部值：', s3.values, type(s3.values))
print('s3全部索引：',s3.index)

