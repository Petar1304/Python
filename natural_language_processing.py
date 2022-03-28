from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize, sent_tokenize
import math
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')


def tf_idf(key , files_num):
	tf = all_words[key]['tf']
	idf = math.log10(files_num / all_words[key]['df'])
	return tf * idf

# input:
corpus_path = input()
doc_path = input()

# testing
# corpus_path = 'C:/Users/kovac/Desktop/camp/public/public/corpus'
# doc_path = 'C:/Users/kovac/Desktop/camp/public/public/corpus/goose/Chinese goose.txt'

stemmer = SnowballStemmer('english')

all_words = dict()
all_sent = dict()

with open(doc_path, 'r', encoding='UTF-8') as f:
	text = f.read()

for word in word_tokenize(text):
	word = word.lower()
	word = stemmer.stem(word)
	if word.isalnum():
		if word not in all_words.keys():
			all_words[word] = {
			# text and document frequency
				'tf': 1,
				'df': 0,
				'tf_idf': 0,
			}

		else:
			all_words[word]['tf'] += 1

files_num = 0

for root, dirs, files in os.walk(corpus_path):
	for file in files:
		files_num += 1
		file_path = os.path.join(root, file)

		with open(file_path, 'r', encoding='UTF-8') as f:
			file_text = f.read()

		file_words = set()
		for w in word_tokenize(file_text):
			w = w.lower()
			w = stemmer.stem(w)
			if w.isalnum():
				file_words.add(w)

		for w in file_words:
			if w in all_words.keys():
				all_words[w]['df'] += 1

for k in all_words:
	val = tf_idf(key = k, files_num = files_num)
	all_words[k]['tf_idf'] = val

# print(sorted_words[0][1]['tf_idf'])
sorted_words = sorted(list(all_words.items()), key=lambda x : x[1]['tf_idf'], reverse=True)

out1 = []
if len(sorted_words) >= 10:
	for i in range(10):
		out1.append(sorted_words[i][0])
else:
	for i in sorted_words:
		out1.append(i[0])

# output 1:
print(', '.join(out1))


########## part 2


for sentence in sent_tokenize(text):
	all_sent[sentence] = {
		'val': 0,
	}


for sent in all_sent.keys():
	top_words = [] # {}
	for word in word_tokenize(sent):
		word = word.lower()
		word = stemmer.stem(word)
		if word.isalnum():
			# all_sent[sent]['val'] += all_words[word]['tf_idf']
		# napravi da se reci mogu ponavljati
			# top_words[word] = {
			# 	'tf_idf': all_words[word]['tf_idf']
			# }
			top_words.append(word)

	if len(top_words) > 10:
		top_words = sorted(top_words, key=lambda x: all_words[x]['tf_idf'], reverse=True)
		# top_words = sorted(list(top_words.items()), key = lambda x: x[1]['tf_idf'], reverse = True)
		top_10 = top_words[:10]

		for w in top_10:
			all_sent[sent]['val'] += all_words[w]['tf_idf']

	else:
		for w in top_words:
			all_sent[sent]['val'] += all_words[w]['tf_idf']

sorted_sent = sorted(list(all_sent.items()), key= lambda x: x[1]['val'], reverse = True)

top_sentences = []
if len(all_sent) > 5:
	for i in range(5):
		top_sentences.append(sorted_sent[i][0])
else:
	top_sentences = all_sent
# print in order of appearance in original text
out2 = []

for sentence in all_sent:
	if sentence in top_sentences:
		out2.append(sentence)

# output 2
print(' '.join(out2))


