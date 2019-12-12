import json
import requests

#r = requests.get('https://cat-fact.herokuapp.com/facts')

#print(r.text)

#print(json.loads(r.text))

r=requests.get('http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json')

r.text
#print(json.loads(r.text))