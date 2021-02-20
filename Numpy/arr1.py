import numpy as np

#generate array
arr = np.array([1,2,3])
arr = np.array([[1,2,3], [4,5,6]])

#functions/methods
arr.shape 
arr.size
arr.ndim #dimensions
arr.data #memory address
np.append(arr, 99) #add but not permanently arr = np.append(arr, element) if you wanna change array
print(np.delete(arr, 1)) #delete but not permanently