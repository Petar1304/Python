from nltk.tokenize import sent_tokenize, word_tokenize

path = 'C:/Users/kovac/Desktop/camp/public/public/corpus/skiing/Alpine skiing.txt'

with open(path, 'r', encoding = 'UTF-8') as f:
	text = f.read()

# print(text)

example_text = 'Hello there! how are you? how are you today and Python is awesome!'

print(sent_tokenize(example_text))