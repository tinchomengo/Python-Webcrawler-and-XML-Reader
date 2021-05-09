'''
Webcrawler that prints span tags and number of tags in url
'''

import urllib.request,urllib.parse
from bs4 import BeautifulSoup
url = ""
html = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")
tags = soup("span")
count=0
for tag in tags:
    y = tag.text
    count+=1
    print(y)
print("\n\n", "The <span> number of tags equals to: ",count, "\n")
