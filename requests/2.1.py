import requests
param={'wd':'mo==莫烦python'}
r=requests.get('https://www.baidu.com/s',params=param)
print(r.url)