import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "连接异常"

def parsePage(tl, txt, html):
    soup = BeautifulSoup(html, 'html.parser')
    r1 = soup.find('div',attrs={'id':'atitle'})
    r2 = soup.find('div',attrs={'id':'acontent'})
    tl.append(r1)
    txt.append(r2)

def printText(tl, txt):
        print(tl[0].text)
        print(txt[0].text)

def main():
    url = input('书籍第一章连接地址：')
    Title = []
    Text = []
    html = getHTMLText(url)
    parsePage(Title, Text, html)
    printText(Title, Text)

main()
