import pandas as pd

data = {
    "goods": ["图书", "文具", "数码"],
    "amount": [120, 80, 500]
}

df = pd.DataFrame(data)
result = df[df["amount"] > 100][["goods", "amount"]]
print(result)