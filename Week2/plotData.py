import numpy as np
import matplotlib.pyplot as plt

matrix = np.loadtxt('data.txt')
print matrix
x = matrix[:,0]
y = matrix[:,1]
print x.T
print y
print np.reshape(y,(-1,1))
plt.plot(x, y, 'ro')
plt.axis([4, 24, -5, 25])
plt.xlabel('y')
plt.ylabel('x')
plt.show()
