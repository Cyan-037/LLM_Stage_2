import pandas as pd

# 读取csv

# df = pd.read_csv(
#     '../data/清洗数据.csv',
#     sep='|'                 # 分隔符，如果不填默认是","
# )

df = pd.read_csv('../data/清洗数据.csv')
print(df)

print('\n缺失值统计')
print(df.isnull().sum())

print('\n非缺失值统计')
print(df.notnull().sum())

print('\n删除含有缺失值的行')
print(df.dropna())        # na: not available

# 删除全部都是缺失值的行，仅部分含有缺失值的行保留
print('\n删除全部是缺失值的行')
print(df.dropna(how='all'))

# 不想删除可以填充
print('\n填充缺失值')
print(df.fillna(0))

print('\n均值填充缺失值')
print(df.fillna(df.mean()))     # mean平均

print('\n最大值填充缺失值')
print(df.fillna(df.max()))      # max最大值

print('\n最小值填充缺失值')
print(df.fillna(df.min()))      # min最小值

