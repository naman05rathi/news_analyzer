import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from goose import Goose
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from sklearn.decomposition import TruncatedSVD




print ("Enter keywords you want to search: ")
string = raw_input()

words = string.split()

length = len(words) - 1

s = ""
for i in range(length):
	s = s+words[i]+'%20'

s = s+words[i+1]

url = 'https://news.google.com/news/search/section/q/'+s

print url

r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")

link_list = []
for link in soup.findAll('a',{'class' : 'nuEeue hzdq5d ME7ew'}):
    link_list.append(link.get('href'))

for link in link_list:
	print link

len_link_list = len(link_list)
print len_link_list

title = []
text = []
final_url = []
for i in range(len_link_list):
	url = link_list[i]
	g = Goose()
	# print url
	article = g.extract(url=url)
	title.append(article.title.encode('ascii', 'ignore'))
	# desc = article.meta_description.encode('ascii', 'ignore')
	text.append(article.cleaned_text.encode('ascii', 'ignore'))
	final_url.append(url)
	print i


df_scrape = pd.DataFrame({'title': title, 'text': text})
df = df_scrape.text

tfidf_vector = TfidfVectorizer(stop_words='english', max_df=.7)
tfidfm = tfidf_vector.fit_transform(df)
# print tfidfm
# print tfidfm.get_shape()
feature_name = tfidf_vector.get_feature_names()
for i in range(0, 20):
    feat_num = random.randint(0, len(feature_name))
    print(feature_name[feat_num])

svd = TruncatedSVD(n_components = 100)

lsa = svd.fit_transform(tfidfm)
print lsa