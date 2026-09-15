import numpy as np
import matplotlib.pyplot as plt     # plot 画板画画
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 准备数据
np.random.seed(36)
x = np.random.randn(50)     # 生成随机50个数
y = x * 2 + np.random.randn(50) * 0.6   # 在x的基础上y有一点偏移

# 画图
plt.figure(figsize=(8,6))
plt.scatter(x,y,color='red')        # scatter散点图

plt.title('测试散点图')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.grid()

plt.show()

