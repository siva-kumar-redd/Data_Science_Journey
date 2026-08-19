import pandas as pd

data = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Salary": [25000, 28000, 30000, 32000, 35000, 38000, 250000]
})

range_data = data["Salary"].max() - data["Salary"].min()
q1 = data["Salary"].quantile(0.25)
q3 = data["Salary"].quantile(0.75)
iqr = q3-q1
lower_bound = q1-1.5*iqr
upper_bound = q3+1.5*iqr
outliers = data[
    (data["Salary"]<lower_bound) | (data["Salary"]>upper_bound)
]
print(range_data)
print(q1)
print(q3)
print(iqr)
print(lower_bound)
print(upper_bound)
print(outliers)