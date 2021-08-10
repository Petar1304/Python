import numpy as np
import pickle

# x = np.random.rand(10)
# pickle_out = open("x.picke", "wb")
# pickle.dump(x, pickle_out)
# pickle_out.close()


pickle_in = open("x.pickle", "rb")
x = pickle.load(pickle_in)
pickle_in.close()

print(x)
