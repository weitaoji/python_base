from bs4 import BeautifulSoup
import requests
baidu=requests.get('https://www.baidu.com').content
print(baidu)
soup=BeautifulSoup(baidu,'html.parser')
#print(soup)
#print(soup.text)
