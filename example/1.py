import numpy as np
m1 = np.matrix("4 3;6 9")
m2 = np.matrix("-2 9;-5 2")
print np.add(m1,m2)
m3 = np.matrix("5;5;2;7")
print np.multiply(2,m3)
u = np.matrix("8;1;4")
print u.T
m4 = np.matrix("4;-4;-3")
m5 = np.matrix("4;2;4")
print "m4.T:"
print m4.T
print "m5"
print m5
print m4.T.dot(m5)
