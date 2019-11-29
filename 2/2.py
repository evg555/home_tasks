import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,21)
y=3*x
y2=(-1/3)*x
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()