import numpy as np
import matplotlib.pyplot as plt
x = 4
theta = 90
sin = np.sin(theta)
cos = np.cos(theta)
print("theta is", theta)
print("sinus is", sin)
print("cosinus is",cos)
print("It is Radian")
meshPoints = np.linspace(-1,1,500)
value53 = meshPoints[52]
print("53th element of meshpoint is",value53)
plt.plot(meshPoints, np.sin(2*np.pi*meshPoints))
plt.show()
