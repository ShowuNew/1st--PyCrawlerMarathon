import requests
import json
import time
headers = {'user-agent': 'my-app/0.0.1'}
res = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers=headers)
#print(res)
js = json.loads(res.text)

for item1 in js['data']:
    print('id:'+str(item1['id']) +' datetime:'+str(time.ctime(item1['created_time'])))
timeList = []
for item1 in js['data']:
    timeList.append(item1['created_time'])
timeList.sort()
print("第一筆回答的時間:",time.ctime(timeList[0]))
print("最後一筆回答的時間:",time.ctime(timeList[len(timeList)-1]))    
