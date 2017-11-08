import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import csv
from bs4 import BeautifulSoup

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
date_list = []
for link in soup.findAll('c-wiz',{'class' : 'M1Uqc kWyHVd'}):
	for l in link.findAll('a', {'class' : 'nuEeue hzdq5d ME7ew'}):
		link_list.append(l.get('href'))
	for d in link.findAll('div', {'class' : 'a5SXAc iYiEmb'}):
		for d1 in d.findAll('span', {'class' : 'oM4Eqe'}):
			for d2 in d1.findAll('span', {'class' : 'd5kXP YBZVLb'}):
				date_list.append(d2.get_text())

final_date = []
print link_list
for i in range(len(date_list)):
	final_date.append(date_list[i].encode('ascii'))

print final_date[1]


thefile = open('links.txt', 'w')
for link in link_list:
	thefile.write("%s\n" % link)