# using python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_str = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url_str)
bs_obj = BeautifulSoup(html, 'lxml')

# list of green tag
name_list = bs_obj.findAll("span", {"class": "green"})
for name in name_list:
    print(name.get_text())

# count of "the prince" appearance
count_list = bs_obj.findAll(text="the prince")
print(len(count_list))
# print(name_list)

# lis of red tag
serif_list = bs_obj.findAll("span", {"class": "red"})
for serif in serif_list:
    print(serif.get_text())


# all_text = bs_obj.findAll(id='tittle')
# print(all_text[0].get_text())
