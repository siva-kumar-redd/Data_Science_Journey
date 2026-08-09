import pandas as pd

data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D", "E", "F", "G"],
    "Purchase": [500, 700, 500, 900, 1200, 500, 800]
})

print(data["Purchase"].mean())
print(data["Purchase"].median())
print(data["Purchase"].mode())
print(data["Purchase"].max())
print(data["Purchase"].min())