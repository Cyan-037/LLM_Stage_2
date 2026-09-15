import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 28, 32],
    '部门': ['技术部', '销售部', '技术部', '人事部', '销售部'],
    '工资': [5000, 7000, 6000, 5500, 7500]
})

print('年龄小于30的数据：\n', df[ df['年龄'] < 30])

print('查看销售部的员工: \n', df.query("部门 == '销售部'"))

print('部门降序，工资升序: \n', df.sort_values(['部门', '工资'], ascending=[False, True]))