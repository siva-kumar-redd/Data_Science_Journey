import pandas as pd
data = pd.Series([10,20,25,30,35,40,45,50,100])

q1 = data.quantile(0.25)
q3 = data.quantile(0.75)

iqr = q3-q1
lower_bound = q1-1.5*iqr
upper_bound = q3+1.5*iqr
outliers = data[(data<lower_bound) | (data>upper_bound)]
print(lower_bound)
print(upper_bound)
print(outliers)