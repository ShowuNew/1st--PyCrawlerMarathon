import json
import requests

r = requests.get('https://cat-fact.herokuapp.com/facts')

print(r.text)

print(json.loads(r.text))
