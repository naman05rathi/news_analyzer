from collections import Counter
import string
import math
import numpy as np



all_documents = []
for i in range(11):
	name = str(i)
	with open(name, 'r') as myfile:
		all_documents.append(myfile.read().replace('\n', ' '))


for doc in all_documents:
	tf = Counter()
	for word in doc.split():
		tf[word] +=1



def build_lexicon(corpus):
	lexicon = set()
	for doc in corpus:
		lexicon.update([word for word in doc.split()])
	return lexicon


def tf(term, document):
	return freq(term, document)


def freq(term, document):
	return document.split().count(term)



vocabulary = build_lexicon(all_documents)

doc_term_matrix = []
for doc in all_documents:
	tf_vector = [tf(word, doc) for word in vocabulary]
	tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
	doc_term_matrix.append(tf_vector)



def l2_normalizer(vec):
	denom = np.sum([el**2 for el in vec])
	return [(el / math.sqrt(denom)) for el in vec]

doc_term_matrix_l2 = []
for vec in doc_term_matrix:
	doc_term_matrix_l2.append(l2_normalizer(vec))



def numDocsContaining(word, doclist):
	doccount = 0
	for doc in doclist:
		if freq(word, doc) > 0:
			doccount +=1
	return doccount 


def idf(word, doclist):
	n_samples = len(doclist)
	df = numDocsContaining(word, doclist)
	return np.log(n_samples / 1+df)



my_idf_vector = [idf(word, all_documents) for word in vocabulary]



def build_idf_matrix(idf_vector):
	idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
	np.fill_diagonal(idf_mat, idf_vector)
	return idf_mat



my_idf_matrix = build_idf_matrix(my_idf_vector)

doc_term_matrix_tfidf = []


for tf_vector in doc_term_matrix:
	doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

doc_term_matrix_tfidf_l2 = []
for tf_vector in doc_term_matrix_tfidf:
	doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))
                                    
#print vocabulary
print np.matrix(doc_term_matrix_tfidf_l2)