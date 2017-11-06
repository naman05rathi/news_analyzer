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
for link in soup.findAll('a',{'class' : 'nuEeue hzdq5d ME7ew'}):
    link_list.append(link.get('href'))

# for link in link_list:
# 	print link

# with open("Output.txt", "w") as text_file:
# 	for link in link_list:
# 		text_file.write("",link)

thefile = open('links.txt', 'w')
for link in link_list:
	thefile.write("%s\n" % link)