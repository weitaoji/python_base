from bs4 import BeautifulSoup
import requests
r=requests.get('https://www.baidu.com').content
soup=BeautifulSoup(r,'html.parser')
#print(soup)#输出html
#print(soup.text)#仅输出文本
#print(soup.prettify())#格式化输出html
#print(soup.title)#输出主题
#print(soup.title.name)#仅输出标签名
#print(soup.title.string)#仅输出主题名字去除标签
#print(soup.title.parent)
#print(soup.title.parent.name)#输出母标签名
#print(soup.p)
#print(soup.p['class'])
#print(soup.a)
#print(soup.find_all('a'))
#print(soup.find(id='link3'))
for link in soup.find_all('a'):#提取页面<a>标记中找到的所有URL：
    print(link.get('href'))
print(soup.get_text())