import pandas as pd

data = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Salary": [25000, 28000, 30000, 32000, 35000, 800000]
})

print("mean salary",data["Salary"].mean())
print("median salary",data["Salary"].median())
print("maximum salary",data["Salary"].max())
print("minimum salary",data["Salary"].min())
