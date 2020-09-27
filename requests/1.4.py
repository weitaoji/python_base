import requests
r1=requests.get('https://api.github.com/events')
r2=requests.get('https://www.baidu.com')
#print(r.text)
#print(r2.encoding)
r2.encoding='utf-8'
print(r2.text)
#print(r2)