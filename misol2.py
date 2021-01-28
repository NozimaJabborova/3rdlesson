import requests
url = 'https://randomuser.me/api/?results=5&gender=female&nat=us,gb'
#p={'results':5&gender=female&nat=UK}
r=requests.get(url)
#print(r.url)
data=r.json()['results']
for i in data:
    print(i['name'],i['nat'])
