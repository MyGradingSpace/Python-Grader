import requests,json

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
    "stduentId" : "",
    "EntityId" : "",
    "markings": [ ]
}


responseBody = {
    "gradingId": "",
    "numOfSubmissions": 0,
    "results" : [ ]
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

