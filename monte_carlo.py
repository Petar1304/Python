import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import random

a = 0
b = np.pi 
N = 1000
    
def func(x):
    return np.sin(x)


areas = []

for i in range(N):
    xrand = np.zeros(N)
    
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0
        
    for i in range(N):
        integral += func(xrand[i])
        
    answer = (b-a)/ float(N)*integral        
    areas.append(answer)

plt.title('Distribution of Areas Calculated')
plt.hist(areas, bins = 30, ec = 'black')    
plt.xlabel('Areas')
plt.show()

