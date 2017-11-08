import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import csv
from bs4 import BeautifulSoup
from goose import Goose
from pattern.en import ngrams


print ("Enter keywords you want to search: ")
string = raw_input()

words = string.split()

length = len(words) - 1

s = ""
for i in range(length):
	s = s+words[i]+'%20'

s = s+words[i+1]

url = 'https://news.google.com/news/search/section/q/'+s

r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")

link_list = []
for link in soup.findAll('a',{'class' : 'nuEeue hzdq5d ME7ew'}):
    link_list.append(link.get('href'))

len_link_list = len(link_list)
print len_link_list

reader = csv.reader(open('nyu_data.csv', 'r'))
word_dict = dict((rows[0],rows[1]) for rows in reader)

text = []
score = []
for i in range(len_link_list):
	url = link_list[i]
	g = Goose()
	article = g.extract(url=url)
	thefile = open(str(i), 'w')
	title = article.title.encode('ascii', 'ignore')
	desc = article.meta_description.encode('ascii', 'ignore')
	text = article.cleaned_text.encode('ascii', 'ignore')

	text1 = ngrams(text, n=1, punctuation=".,;:!?()[]{}`''\"@#$^&*+-|=~_", continuous=False)
	dictionary = {}
	pos_score, neg_score = 0, 0
	for x in text1:
		if word_dict.has_key(x[0]):
			dictionary[x[0]] = word_dict[x[0]]

	pos_list = []
	neg_list = []

	for key, value in dictionary.iteritems():
		if value == 'positive':
			pos_list.append(key)
		if value == 'negative':
			neg_list.append(key)

	pos_score = len(pos_list)
	neg_score = len(neg_list)
	# print pos_list
	# print neg_list

	count = pos_score + neg_score
	if count == 0:
		total_score = 0
	else:
		total_score = float(pos_score) / float(count)
	variable = [link_list[i], total_score]
	score.append(variable)


for s in score:
	print s