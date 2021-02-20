import numpy 

x = numpy.zeros((2,3), dtype = int)
	
#	[[0 0 0]
#	 [0 0 0]]
	
x = numpy.ones((4, 5), dtype = int)

x = numpy.arange(10) #[0 1 2 3 4 5 6 7 8 9]

x = numpy.linspace(1, 4, 6) #(start, end, number of steps)

x = numpy.full((2,2), 8)

x = numpy.eye(5) 

#[[1. 0. 0. 0. 0.]
#[0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]
# [0. 0. 0. 0. 1.]]

x = numpy.random.random((4,5)) #random array

print(x)