import requests
import os

from bs4 import BeautifulSoup#here
from PIL import Image
url = 'https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html'
resp = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(resp.text)

try:
    os.makedirs( './Data', exist_ok=True )
   
except:
    print('新增資料夾發生錯誤！')

image_tags = soup.find(id='main-content').findChildren('a', recursive=False)

for item in image_tags:
    if 'imgur' not in item['href']:
        continue
    img_id = item['href'].split('/')[-1]
    #print(img_id)
    img_url = 'https://i.imgur.com/{}.jpg'.format(img_id)
    #print(img_url)
    with requests.get(img_url, stream=True) as r:
        if r.status_code == 200:
            img = Image.open(r.raw)
            print(img.format)