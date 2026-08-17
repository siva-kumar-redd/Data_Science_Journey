import pandas as pd

data = pd.Series([10,20,30,40,50,60,70])

q1=data.quantile(0.25)
q2=data.quantile(0.50)
q3=data.quantile(0.75)

print(q1)
print(q2)
print(q3)