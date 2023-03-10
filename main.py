import numpy

v = numpy.array([[1, 5, 1],
     [1, 4, 1],
     [1, 3, 1],
     [-1, 3, 1],
     [-1, -2, 1],
     [-2, 0, 1],
     [-1, 3, 1],
     [-2, 2, 1],
     [-1, 1, 1],
     [-1, -1, 1],
     [-1, 0, -1],
     [-1, -1, -1],
     [-1, 1, -1],
     [-3, -2, -1],
     [-4, -1, -1],
     [-2, -1, -1],
     [-2, -2, -1],
     [-3, 1, -1],
     [-3, -4, -1],
     [2, -1, -1]])

vt = numpy.array(v).transpose()
vm = vt.dot(v)
vm = vt @ v
print(vt)
det = numpy.linalg.det(vm)
print("************************")
print(det)
mvm = numpy.linalg.inv(vm)
print(vm)
#

