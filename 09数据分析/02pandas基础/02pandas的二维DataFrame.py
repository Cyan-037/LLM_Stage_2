import pandas as pd
import numpy as np

# 基于字典
data = {
    '姓名': ['张三','李四','王五','赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京','上海','广州','深圳'],
    '工资': [5000, 7000, 6000, 8000]
}   # key就是列名，value是列表，当前列的每一行数据
df1 = pd.DataFrame(data)
print(df1)
print(type(df1))
