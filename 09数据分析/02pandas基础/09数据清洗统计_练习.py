import pandas as pd

df = pd.read_csv('../data/products.csv')
print(df, type(df))

# 读取products.csv转为pandas的DataFrame，删除缺失值的行
# 剩余内容，按自营非自营分组，统计平均价格
df.dropna(inplace=True)
print('\n删除缺失值的行：\n', df)

result_df = df.groupby('is_self')['price'].mean()
print('\n按自营非自营分组，统计平均价格：\n', result_df)

