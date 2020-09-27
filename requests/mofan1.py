from bs4 import BeautifulSoup
import requests
URL='https://www.nationalgeographic.com/animals/'
html=requests.get(URL).text
soup=BeautifulSoup(html,'lxml')
img_ul=soup.find_all('ul',{'class':'img_list'})
print(len(img_ul))