import requests,json

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)
# r = requests.post('https://pretty-printed-request-bin.herokuapp.com/1okv8jl1', data=open('test.json','rb'))
# print(r.status_code)
# print(r.content)

submission = {
    "output" : "",
    "expectOutput" : "",
    "match" : ""
}

grades = {
    "taskname"  : "",
    "testCase"  : "",
    "CaseNumber": 0,
    "submissions" : { }
}

results = {
    "studentName" : "",
    "stduentId" : "",
    "fileId" : "",
    "fileName" : "",
    "grades": { }
}

responseBody = {
    "gradingId": "",
    "numOfSubmissions": 0,
    "results" : { }
}

# data = {'Eleven': 'Millie',
#         'Mike': 'Finn',
#         'Will': 'Noah'}
# with open('app.json', 'w') as fp:
#     json.dump(data, fp)
