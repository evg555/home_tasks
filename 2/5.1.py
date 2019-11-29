import matplotlib.pyplot as plt
import numpy as np

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

d = -point.dot(normal)
xx, yy = np.meshgrid(range(10), range(10))
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
z2 = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2] + 5

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z)
plt3d.plot_surface(xx, yy, z2)
plt.show()