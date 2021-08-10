# sin and cos functions

import numpy as np
import matplotlib.pyplot as plt

# Domains
x = np.linspace(0, 4*np.pi, 1000)

# Amplitudes
A1 = 1
A2 = 1

# Kruzne ucestalosti
w1 = 1
w2 = 1

# Fazne razlike
f1 = 0 * np.pi
f2 = 1/2 * np.pi

def func(A, x, w, f):
    y = A * np.cos(w*x + f)
    return y

y1 = func(A1, x, w1, f1)
y2 = func(A2, x, w2, f2)
    
plt.figure(1)
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.show()
