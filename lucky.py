#! python3

import requests
import sys
import webbrowser
import bs4

print('Wyszukiwanie...')
res = requests.get('http://google.pl/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status

soup = bs4.BeautifulSoup(res.text, features="lxml")

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))