import pandas as pd
import numpy as np

s = pd.Series(data=[1, 4, 7], index=[0, 1, 2], dtype=int, name='ime')
# data -> podaci serije
# index -> labele na osnovu kojih se pristupa podacima
# dtype -> tip podataka
# name -> ime serije

# print(s.index.values)
# print(s.values)
# print(s.shape)
# print(s.hasnans) # da li postoje NaN-ovi
sc = s.astype(dtype=float, copy=True)
# konverzija podataka u drugi tip uz vracanje kopije
# sc_numpy = s.to_numpy()
# sc_list = s.to_list()

# s.get(0)
# dohvatanje vrednosti
s.at[3] = 4
s.at[4] = 5
# print(s)

s.iat[0] # pristup preko indeksa

s.dropna()
s.fillna(0)
s.replace(np.nan, 0)


df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
				  index=[0, 1, 2], columns=['a', 'b', 'c'], dtype=int)

