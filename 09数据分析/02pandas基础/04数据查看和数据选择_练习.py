import pandas as pd

data_list = [
    ['01', '张三', 25],
    ['02', '李四', 30],
    ['03', '王五', 35],
    ['04', '赵六', 28]
]

df = pd.DataFrame(
    data_list,
    columns=['id', 'name', 'age'],
    index=['s1', 's2', 's3', 's4']
)
print(df)

print('前两行：\n', df.head(2))
print('后两行：\n', df.tail(2))

# loc用行索引
print('第一行和第三行：\n', df.loc[['s1','s3']])
# iloc用列索引
print('第一行和第三行：\n', df.iloc[[0,2]])

print('name和age列：\n', df.loc[:][['name', 'age']])
print('name和age列：\n', df[['name', 'age']])