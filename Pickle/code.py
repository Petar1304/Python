import torch
import pickle

X = torch.rand([500, 50, 50])

# Saving
pickle_out = open("X.pickle", "wb")
pickle_out.close()
pickle.dump(X, pickle_out)

# Reading
pickle_in = open("X.pickle", "rb")
Y = pickle.load(pickle_in)
pickle_in.close()
