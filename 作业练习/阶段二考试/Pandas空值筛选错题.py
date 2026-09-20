'''
哪里出错？改正
'''
import pandas as pd

data = {
    "name": ["张三", "李四", "王五", "赵六"],
    "late_count": [2, None, 0, None]
}
df = pd.DataFrame(data)
# 筛选迟到次数不为空的数据
res = df[df["late_count"].notnull()]
print(res)