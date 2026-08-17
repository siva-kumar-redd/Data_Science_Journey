import numpy as np

data = np.array([10,20,30,40,50,60,70])

q1=np.percentile(data,25)
q2=np.percentile(data,50)
q3=np.percentile(data,75)

print(q1)
print(q2)
print(q3)