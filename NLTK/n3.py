from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('english')

example_worlds = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']

for w in example_worlds:
	print(stemmer.stem(w))

print(stemmer.stem('once'))