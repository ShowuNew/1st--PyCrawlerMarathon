import requests
import json
r = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=true')
data = json.loads(r.text)

#print(len(data))
#print(data[0])
#k=data[0]
#print(k.keys())


# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
for i in data:
    print(i["title"]+i["createdAt"]+str(i["commentCount"])+str(i["likeCount"]))
    #print()