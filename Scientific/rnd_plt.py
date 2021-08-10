import numpy as np 
import matplotlib.pyplot as plt

loop = True
while loop:
	n = input()
	if n == 'False':
		loop = False
	else:
		x = []
		y = []
		for _ in range(int(n)):
			x.append(np.random.rand())
			y.append(np.random.rand())
		plt.plot(x, y, 'r.')
		plt.show()