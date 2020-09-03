import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.biqu.ge/182/182709/46085598.html'
cha = 10
for i in range(cha):
    t = url.split('/')[-1]
    num = eval(re.findall(r'\d{8}', t)[0])
    num += i
    new_url = 'http://www.biqu.ge/182/182709/' + str(num) + '.html'
    r = requests.get(new_url)
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', attrs={'id':'atitle'})
    cont = soup.find('div', attrs={'id':'acontent'})
    print(title.text)
    print(cont.text)
