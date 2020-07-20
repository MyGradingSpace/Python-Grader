import requests,json
#send
testResult = {
    "output" : "",
    "expectOutput" : "",
    "match" : True,
    "marks" : 0
}

markings = {
    "filename" : "",
    "marked" : True,
    "testResult" : [ ]
}

results = {
    "studentID" : "",
    "EntityId" : "",
    "markings": [ ]
}


responseBody = {
    "gradingId": "",
    "numOfSubmissions": 0,
    "results" : [ ]
}
#receive
testCases = {
    "input" : "",
    "output" : "",
    "marks" : 0
}

configuration = {
   "filename" : "",
   "testCases" : [ ]
}

links = {
    "EntityId" : "",
    "filename" : "", #zip
    "link" : ""
}

receiveBody={
    "gradingId" : "",
    "links" : [ ],
    "configuration" : [ ]
}

def add_testResult(testResult,markings):
    markings["testResult"].append(testResult)
    return 

def add_markings(markings,results):
    results["markings"].append(markings)
    return 

def add_results(results,responseBody):
    responseBody["results"].append(results)
    return 

