import numpy as np
import math

x1 = np.array([10,10,10])
x2 = np.array([0,0,-10])
sum = x1 + x2
len = math.sqrt(sum[0]**2+sum[1]**2+sum[2]**2)

print(sum)
print(len)
