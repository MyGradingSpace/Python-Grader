import requests
import json

r = requests.get('http://backend-test-my-grading-space.apps.us-east-1.starter.openshift-online.com:80/joblinks',params={"gradingId" : "2020-6-CP317T1-Dropbox-VESo"},headers={"key":"oursecret"}, timeout=5)

print(r.content)