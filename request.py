import requests
import json

r = requests.get('http://localhost:5000/joblinks',params={"gradingId" : "2020-6-CP317T1-Dropbox-VESo"},headers={"key":"oursecret"}, timeout=5)

print(r.content)