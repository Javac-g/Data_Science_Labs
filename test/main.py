import numpy
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('data.txt')
X = data[:, 0:3]

X1 = X[0:10]  # 10*2
x2 = X[10:20]

V = np.array(X)
vt = numpy.transpose(V)
print(vt)




