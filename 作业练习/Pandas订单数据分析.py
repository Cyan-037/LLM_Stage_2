import pandas as pd

orders = [
    {"category": "图书", "price": 30, "count": 4},
    {"category": "文具", "price": 5, "count": 20},
    {"category": "图书", "price": 45, "count": 2},
    {"category": "数码", "price": 300, "count": 1},
    {"category": "文具", "price": 8, "count": 10}
]

df = pd.DataFrame(orders)
df['amount'] = df['price'] * df['count']

# as_index=False将分组键不要保留为索引而是普通列
result = df.groupby('category', as_index=False)['amount'].sum()
result = result.sort_values(['amount'], ascending=False)

print(result)