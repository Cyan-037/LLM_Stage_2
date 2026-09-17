import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

sales = [
    {"month": "1月", "category": "图书", "amount": 1200},
    {"month": "1月", "category": "文具", "amount": 800},
    {"month": "2月", "category": "图书", "amount": 1500},
    {"month": "2月", "category": "文具", "amount": 950},
    {"month": "3月", "category": "图书", "amount": 1800},
    {"month": "3月", "category": "文具", "amount": 1100}
]

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(sales)

month_total = df.groupby("month")["amount"].sum()
category_total = df.groupby("category")["amount"].sum()

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
month_total.plot(kind="line", marker="o")
plt.title("月度销售额趋势")
plt.xlabel("月份")
plt.ylabel("销售额")

plt.subplot(1, 2, 2)
category_total.plot(kind="bar")
plt.title("分类销售额对比")
plt.xlabel("商品分类")
plt.ylabel("销售额")

plt.tight_layout()
plt.show()