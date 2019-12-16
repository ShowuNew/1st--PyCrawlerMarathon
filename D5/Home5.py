import requests
import json
r = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=true')
data = json.loads(r.text)

print(len(data))
#print(data[0])
#k=data[0]
#print(k.keys())


# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
#for i in data:
#    print(i["title"]+i["createdAt"]+str(i["commentCount"])+str(i["likeCount"]))
#    #print()

sum_commentCount=0
sum_likeCount=0
# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
for i in data:
    sum_commentCount+=int(i["commentCount"])
    sum_likeCount+=int(i["likeCount"])


print(sum_commentCount/len(data))
print(sum_likeCount/len(data))

r = requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=false')
data = json.loads(r.text)

sum_commentCount=0
sum_likeCount=0
for n in data:
    sum_commentCount+=int(n["commentCount"])
    sum_likeCount+=int(n["likeCount"])


print(sum_commentCount/len(data))
print(sum_likeCount/len(data))