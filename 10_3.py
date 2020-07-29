import numpy as np
import matplotlib.pyplot as plt
#1
x = np.linspace(0,10,100)
f = np.exp(-x/10)*np.sin(np.pi*x)
g = x*np.exp(-x/3)
plt.plot(x,f,x,g)
plt.legend(['f(x)', 'g(x)'])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#2
theta = np.linspace(0,2*np.pi,100)
r=0.8+np.cos(theta)
x2=r*np.cos(theta)
y2=r*np.sin(theta)
plt.plot(x2,y2)

r=1.0+np.cos(theta)
x2=r*np.cos(theta)
y2=r*np.sin(theta)
plt.plot(x2,y2)

r=1.2+np.cos(theta)
x2=r*np.cos(theta)
y2=r*np.sin(theta)
plt.plot(x2,y2)

plt.legend(['r=0.8','r=1.0','r=1.2'])
plt.show()
