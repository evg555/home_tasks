import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
xgrid, ygrid = np.meshgrid(x, y)

zgrid = xgrid **2 + ygrid
zgrid2 = xgrid **2 + 2*ygrid**2

fig = plt.figure()
axes = Axes3D(fig)
axes.plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=1)
axes.plot_surface(xgrid, ygrid, zgrid2, rstride=1, cstride=1)
plt.show()