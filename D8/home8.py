import requests
from bs4 import BeautifulSoup
import json
r = requests.get('https://www.dcard.tw/f')
r.encoding = 'utf-8'
#print(r.text)
#print(type(r.text))
#data = json.loads(r.text)

b = BeautifulSoup(r.text)
#print(b)
print(type(b))

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
rr = requests.get('https://www.zhihu.com/explore',headers=headers)
rr.encoding = 'utf-8'
#print(rr.text[0:600])