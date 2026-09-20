'''
背景：
某文具店想统计不同商品分类的销售总额，并找出销售表现较好的分类。为了让结果更直观，还需要将各分类销售总额绘制成柱状图。

'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

orders = [
    {"category": "图书", "amount": 120},
    {"category": "文具", "amount": 80},
    {"category": "图书", "amount": 200},
    {"category": "数码", "amount": 500},
    {"category": "文具", "amount": 150}
]

df = pd.DataFrame(orders)
cg = df.groupby('category', as_index=False)['amount'].sum()
print(cg)
print(cg[cg['amount'] > 200])

x = plt.bar(cg['category'], cg['amount'], color='steelblue')
plt.title('各分类销售总额柱状图')
plt.xlabel('分类')
plt.ylabel('销售总额')
plt.grid()
plt.tight_layout()

plt.show()