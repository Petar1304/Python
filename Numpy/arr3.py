import numpy

x = numpy.array([[1,2], [3,4]])
y = numpy.array([[5,6], [7,8]])

z = x + y
#same
z = numpy.add(x,y)

z = x - y
z = numpy.subtract(x, y)

z = x * y
z = numpy.multiply(x, y)

z = x / y

z = numpy.sqrt(x)

v = numpy.array([9, 10])
w = numpy.array([11, 13])

z = v.dot(w) #dot product
z = numpy.dot(v, w)

z = numpy.dot(x, y)

z = numpy.sum(x)

z = numpy.sum(x, axis = 0)

print(z)