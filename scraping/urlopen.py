from urllib.request import urlopen
#if has chiese,apply decode()
html=urlopen("https://www.baidu.com/").read().decode('utf-8')
print(html)