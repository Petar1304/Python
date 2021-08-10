# infinite square well
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = 2 * np.pi
    x = np.linspace(0, a, 1000)
    A = np.sqrt(2/a) # normalization constant

    def psi(n, x):
        wf = A*np.sin(n*np.pi*x/a)
        return wf

    y = []
     
    y1 = psi(1, x)
    y2 = psi(2, x)
    y3 = psi(3, x)

    plt.figure(1)
    plt.plot(x, y1, 'b', linewidth=2, label='n=1')
    plt.plot(x, y2, 'r', linewidth=1.7, label='n=2')
    plt.plot(x, y3, 'k', linewidth=1.7, label='n=3')
    plt.axvline(0)
    plt.axvline(np.pi*2)
    plt.title('Wavefunction for Infinite Square Well')
    plt.xlabel('x values')
    plt.ylabel('$\psi(x)$')
    plt.legend()
    plt.grid()
    plt.show()
