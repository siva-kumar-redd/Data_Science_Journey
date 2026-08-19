import numpy as np

values = np.array([10,20,30,40,50,60,70])
range_value = np.max(values)-np.min(values)

q1 = np.percentile(values,25)
q3 = np.percentile(values,75)

iqr = q3-q1

print("Q1",q1)
print("Q3",q3)
print("range",range_value)
print("IQR",iqr)