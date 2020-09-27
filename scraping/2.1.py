from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen('https://www.baidu.com/').read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
print(html)
#all_href=soup.find_all('a')
#print(all_href)