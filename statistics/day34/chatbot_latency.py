import pandas as pd


latency = [1.1, 1.2, 1.3, 1.4, 1.5, 15.0]
data = pd.Series(latency)

print(data.mean())
print(data.median())
print(data.max())