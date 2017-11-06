from goose import Goose

with open('links.txt') as f:
    link_list = f.read().splitlines()

length = len(link_list)
i = 6
for i in range(7):
	url = link_list[i]
	g = Goose()
	article = g.extract(url=url)
	thefile = open(str(i), 'w')
	title = article.title.encode('ascii', 'ignore')
	desc = article.meta_description.encode('ascii', 'ignore')
	text = article.cleaned_text.encode('ascii', 'ignore')
	title_split = title.split(" ")
	desc_split = desc.split(" ")
	text_split = text.split(" ")
	for word in title_split:
		thefile.write(word+"\n")
	for word in desc_split:
		thefile.write(word+"\n")
	for word in text_split:
		thefile.write(word+"\n")

# for link in link_list:
# 	

# g = Goose()
# article = g.extract(url=url)
# print article.title
# print article.meta_description
# print article.cleaned_text