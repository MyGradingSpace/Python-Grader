import requests,json
test={
    "gradingId": "whatever",
    "links": [
        {
            "EntityId": 123456789,
            "filename" : "youx8420_a02.zip",
            "link": "https://github.com/fleiray/Fangjian/files/4967411/youx8420_a02.zip"
        },
        {
            "EntityId": 123456790,
            "filename" : "leix5490_a02.zip",
            "link": "https://github.com/fleiray/Fangjian/files/4967409/leix5490_a02.zip"
        }
    ],
    "configuration": [
        {
            "filename": "a2q1.c",
            "testCases": [
                {
                "input": "",
                "output": "need more than two integer arguments: 2 1 2 3 4",
                "marks": 1
            },
            {
                "input": "1 2 3 4",
                "output": "2*1^2 + 3*1^1 + 4*1^0 = 9",
                "marks": 1
            },
            {
                "input": "10 9 8 7 6 5 4",
                "output": "9*10^5 + 8*10^4 + 7*10^3 + 6*10^2 + 5*10^1 + 4*10^0 = 987654",
                "marks": 1
            }
            ]
        },
        {
        "filename": "a2q2.c",
        "testCases": [
            {
            "input": "",
            "output": "need more than two integer arguments: 2 1 2 3 4",
            "marks": 1
        },
        {
            "input": "1 2 3 4",
            "output": "2*1^2 + 3*1^1 + 4*1^0 = 9",
            "marks": 1
        },
        {
            "input": "10 9 8 7 6 5 4",
            "output": "9*10^5 + 8*10^4 + 7*10^3 + 6*10^2 + 5*10^1 + 4*10^0 = 987654",
            "marks": 1
        },
        {
            "input": "5 6 7",
            "output": "6*5^1 + 7*5^0 = 37",
            "marks": 1
        },
        {
            "input": "4",
            "output": "need more than two integer arguments: 2 1 2 3 4",
            "marks": 1
        }
        ]
    }
]
}
#send
testResult = {
    "output" : "",
    "expectOutput" : "",
    "match" : False,
    "marks" : 0
}

markings = {
    "filename" : "",
    "marked" : False,
    "testResult" : [ ]
}

results = {
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

runC = {
    "EntityId" : "",
    "results" : []
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

