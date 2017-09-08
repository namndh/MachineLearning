from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

X = np.array([[1,2,4,0]]).T
y = np.array([[0.5,1,2,0]]).T
# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
regr = linear_model.LinearRegression(fit_intercept=False) # fit_intercept = False for calculating the bias
regr.fit(Xbar, y)

# Compare two results
print( 'Solution found by scikit-learn  : ', regr.coef_ )
print( 'Solution found by (5): ', w.T)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 6, 5)
y0 = w_0 + w_1*x0
print ("w_0 = ",w_0)
print ("w_1 = ",w_1)
# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([0, 10, 0, 10])
plt.xlabel('y')
plt.ylabel('x')
plt.show()
