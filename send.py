import requests
import json
fdata =open("send.json","rb")
# print(json.dump(fdata))
# r = requests.put('https://pretty-printed-request-bin.herokuapp.com/1kvflzr1',data=fdata, headers={"key":"oursecret","Content-Type":"application/json"}, timeout=5)
r = requests.put('http://backend-test-my-grading-space.apps.us-east-1.starter.openshift-online.com:80/grading',data=fdata, headers={"key":"oursecret","Content-Type":"application/json"}, timeout=5)
print(r.status_code)
print(r.content)
