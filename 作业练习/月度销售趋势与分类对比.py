import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def plot_sales(df):
    month_total = df.groupby('month', as_index=False)['amount'].sum()
    category_total = df.groupby('category', as_index=False)['amount'].sum()

    print(month_total)
    print(category_total)

    plt.figure(figsize=(10, 4))

    # 左图：月度趋势
    plt.subplot(1, 2, 1)
    plt.plot(month_total['month'], month_total['amount'],
             color='steelblue', marker='o')
    plt.title('月度销售额趋势')
    plt.xlabel('月份')
    plt.ylabel('销售额')
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # 右图：分类对比
    plt.subplot(1, 2, 2)
    plt.bar(category_total['category'], category_total['amount'],
            color='steelblue')
    plt.title('分类销售额对比')
    plt.xlabel('商品分类')
    plt.ylabel('销售额')
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    sales = [
        {"month": "1月", "category": "图书", "amount": 1200},
        {"month": "1月", "category": "文具", "amount": 800},
        {"month": "2月", "category": "图书", "amount": 1500},
        {"month": "2月", "category": "文具", "amount": 950},
        {"month": "3月", "category": "图书", "amount": 1800},
        {"month": "3月", "category": "文具", "amount": 1100}
    ]

    df = pd.DataFrame(sales)
    plot_sales(df)