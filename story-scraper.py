from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")
url = "http://textfiles.com/stories/"
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

par = ''
i = 1
for l in links[1::]:
    link = url+l
    try:
        s = requests.get(url+l).text
    except:
        pass
    for j in ((s.replace('\n', ' ').replace('\r', ' ')).split()):
        if j != u'':
            par+=j.strip()+u' '
    print l, "\t:\tutils.py{:0.2f}% finished.".format(100*(float(i)/len(links)))
    i+=1

par =par.replace(u',', '')
par =par.replace(u'.', ' .')
par =par.replace(u'"', ' " ')
par =par.replace(u'!', ' !')
par =par.replace(u'?', ' !')
par =par.strip(u'()[]')
