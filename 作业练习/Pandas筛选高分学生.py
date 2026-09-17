'''
背景：
班主任想快速找出成绩优秀的学生。现在有一份简单的学生成绩数据，需要筛选出分数大于 80 的学生。
问题：
使用 Pandas 创建学生成绩数据，包含 name 和 score 两列，输出分数大于 80 的学生。
'''

import pandas as pd

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 76},
    {"name": "王五", "score": 92},
    {"name": "赵六", "score": 80},
    {"name": "钱七", "score": 68},
    {"name": "孙八", "score": 88}
]

df = pd.DataFrame(students)
print('分数大于80的学生:\n',df[df['score']>80])
