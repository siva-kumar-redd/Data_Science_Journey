import numpy as np

values = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
])

print("P90:", np.percentile(values, 90))
print("P95:", np.percentile(values, 95))
print("P99:", np.percentile(values, 99))