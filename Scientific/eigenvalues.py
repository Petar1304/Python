import numpy as np

# A = np.mat("1, 2, 3; 4, 5, 6; 7, 8, 9")
# A = np.random.randint(9, size=(3, 3))
A = np.mat("3 -1 2; 3 -1 6; -2 2 -2")

print(A)

eigenvals, eigenvec = np.linalg.eig(A)

for i in range(len(eigenvals)):
    print(f"Eigenvalue {i+1}: {eigenvals[i]}\nEigenvector {i+1}: {eigenvec[i]}")
