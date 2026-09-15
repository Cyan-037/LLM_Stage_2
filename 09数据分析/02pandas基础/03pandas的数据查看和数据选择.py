import pandas as pd

# 创建实例DataFrame
data_list = [
    ['张三', 25, '北京', 5000],
    ['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],
    ['赵六', 28, '深圳', 8000]
]

# 手动指定行列索引的名字（默认都是0、1、2）    column列 row行
df = pd.DataFrame(
    data_list,
    columns=['姓名','年龄','地址','薪资'],       # 手动提供列索引
    index=['row1','row2','row3','row4']
)
print(df)
print('='*20)

# 查看前两行
print(df.head(2))
print('='*20)

# 查看尾2行
print(df.tail(2))
print('='*20)

# 查看df整体的描述信息
print('df信息：\n', df.describe())
print('='*20)

# 选择列
# 单独看姓名列： select 姓名 from 表;
# df[列索引]   df[3]   df['姓名']
print('姓名：\n', df['姓名'])
print('列类型：\n', type(df['姓名']))     # Series
print('='*20)

# 看姓名和年龄列
# select 姓名，年龄 from 表
# 语法： df[[列索引, 列索引, ...]]
print('姓名, 年龄列: \n', df[['姓名', '年龄']])
print('='*20)

# 通过行索引选择 df.loc[[列索引，列索引]]
print('第一行： \n', df.loc['row1'])
print('='*20)
print('第一行和第三行： \n', df.loc[['row1', 'row3']])

# 切片
print('切片：\n', df["row1": "row3"])  # 切片尾巴是包含

# 行索引默认0123...是一直存在，如果你手动设置了行索引，那么0123也存在，还是可以用
# df.iloc 用0123
# df.loc 用行索引
print('第一行： \n', df.iloc[0])
print('第一第三行：\n', df.iloc[[0,2]])
print('前三行：\n', df.iloc[0:3])