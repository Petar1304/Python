import numpy as np
import matplotlib.pyplot as plt

N = 10000

squareX = []
squareY = []
circleX = []
circleY = []

for _ in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1) 
    if x**2 + y**2 <= 1:
        circleX.append(x)
        circleY.append(y)
    else:
        squareX.append(x)
        squareY.append(y)

pi = 4 * len(circleX)/float(N)


print(f'pi calculated: {pi}\nactual pi: {np.pi}')
plt.plot(squareX, squareY, 'b.')
plt.plot(circleX, circleY, 'r.')
plt.grid()
plt.show()
