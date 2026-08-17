import pandas as pd

data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Spending": [300, 400, 500, 600, 700, 900, 1200, 5000]
})

print("P25:", data["Spending"].quantile(0.25))
print("P50:", data["Spending"].quantile(0.50))
print("P75:", data["Spending"].quantile(0.75))
print("P90:", data["Spending"].quantile(0.90))