import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from goose import Goose
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB



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
	if link_list[i] == "http://aa.com.tr/en/economy/turkish-stocks-down-nearly-15-percent-at-close/961252":
		continue
	url = link_list[i]
	g = Goose()
	print url
	article = g.extract(url=url)
	title.append(article.title.encode('ascii', 'ignore'))
	# desc = article.meta_description.encode('ascii', 'ignore')
	text.append(article.cleaned_text.encode('ascii', 'ignore'))
	final_url.append(url)
	print i


df_scrape = pd.DataFrame({'title': title, 'text': text})
# print df_scrape.head()
df_s = df_scrape.text
df_data = pd.read_csv('fakereal.csv')
# print df_data.shape
# print df_data.head()

df_y = df_data.label
df_data = df_data.text 
# print type(df_y)
# print type(df_data)
# print df_y.head()
# print df_data.head()
# print df_data.shape


tfidf_vector = TfidfVectorizer(stop_words='english', max_df=.7)
tfidf_train = tfidf_vector.fit_transform(df_data)
tfidf_test = tfidf_vector.transform(df_s)

tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vector.get_feature_names())

clf = MultinomialNB() 
clf.fit(tfidf_train, df_y)
pred = clf.predict(tfidf_test)


print('\n')
for i in range(len(final_url)):
	print final_url[i]
	print pred[i]
	print('\n')
