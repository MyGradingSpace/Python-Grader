import requests

fdata =open("test.json","rb")
r = requests.post('https://pretty-printed-request-bin.herokuapp.com/1mun6oe1', data=fdata)
print(r.status_code)
print(r.content)