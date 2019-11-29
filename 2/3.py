import matplotlib.pyplot as plt
import numpy as np

#Окружность
x = np.linspace(-1,1,100)
y1 = [np.sqrt(1-i**2) for i in x]
y2 = [-np.sqrt(1-i**2) for i in x]

#Эллипс
x2 = np.linspace(-5,5,100)
y3 = [np.sqrt(9*(1-i**2/25)) for i in x2]
y4 = [-np.sqrt(9*(1-i**2/25)) for i in x2]

#Гипербола
x3 = np.linspace(-10,10,1000)
y5 = [np.sqrt(9*(i**2/25-1)) for i in x3]
y6 = [-np.sqrt(9*(i**2/25-1)) for i in x3]

plt.figure(1,[12,5])
plt.subplot(1,3,1)
plt.plot(x,y1, 'b-',x,y2,'b-')
plt.axis('equal')
plt.grid()

plt.subplot(1,3,2)
plt.plot(x2,y3, 'b-',x2,y4,'b-')
plt.axis('equal')
plt.grid()

plt.subplot(1,3,3)
plt.plot(x3,y5, 'b-',x3,y6,'b-')
plt.axis('equal')
plt.grid()

plt.show()