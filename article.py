from goose import Goose

with open('links.txt') as f:
    link_list = f.read().splitlines()

length = len(link_list)

for i in range(length):
	url = link_list[i]
	g = Goose()
	article = g.extract(url=url)
	thefile = open(str(i), 'w')
	thefile.write(article.title.encode('ascii', 'ignore'))
	thefile.write(article.meta_description.encode('ascii', 'ignore'))
	thefile.write(article.cleaned_text.encode('ascii', 'ignore'))

# for link in link_list:
# 	

# g = Goose()
# article = g.extract(url=url)
# print article.title
# print article.meta_description
# print article.cleaned_text