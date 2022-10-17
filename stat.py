import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.mean(speed)
print(x)
y = np.median(speed)
print(y)
z = stats.mode(speed)
print(z)
v = np.var(speed)
print(v)
s = np.std(speed)
print(s)
