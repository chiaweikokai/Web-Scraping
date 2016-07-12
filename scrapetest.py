from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError
from urllib.error import URLError

# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# print(html.read())

try:
    # html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as err:
    print(err)
except URLError as err:
    print("This server could not be found!")
else:
    print("It works.")

# bsObj = BeautifulSoup(html.read(), "lxml")
# print(bsObj.h1)


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title

title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)




