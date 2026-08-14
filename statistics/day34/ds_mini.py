import pandas as pd

data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Purchase": [500, 550, 600, 650, 700, 750, 800, 10000]
})

print(data["Purchase"].mean())
print(data["Purchase"].median())
print(data["Purchase"].mode())
print(data["Purchase"].min())
print(data["Purchase"].max())