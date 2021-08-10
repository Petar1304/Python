import numpy as np
import matplotlib.pyplot as plt

N = 1000000

squareX = []
squareY = []
circleX = []
circleY = []

for i in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1) 
    if x**2 + y**2 <= 1:
        circleX.append(x)
        circleY.append(y)
    else:
        squareX.append(x)
        squareY.append(y)

    if i == N/10:
        print('10%')
    if i == N*0.25:
        print('25%')
    if i == N/2:
        print('50%')
    if i == 0.75*N:
        print('75%')
    if i == N-1:
        print('100%')


pi = 4 * len(circleX)/float(N)

print(f'Pi calculated: {pi}\nNumpy pi: {np.pi}\nAccuracy {100*(pi/np.pi)}%')

plt.figure(1)
plt.plot(squareX, squareY, 'b.')
plt.plot(circleX, circleY, 'r.')
plt.grid() 
plt.show()