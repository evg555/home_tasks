import numpy as np
import matplotlib.pyplot as plt
import math
x = []
y = []

for i in range(-3.14,math.pi, 3.14):
    x_ = i/100000
    x.append(x_)
    y1.append(math.sqrt((1+x_**2)/a**2)*b**2)
    y2.append(-math.sqrt((1 + x_ ** 2) / a ** 2) * b ** 2)
y = math.sin(x)/x
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()