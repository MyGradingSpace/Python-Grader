from data_structure import *
test={
    "gradingId" : "",
    "configuration" : [ 
        
        {
        "filename" : "xxx",
        "testCases" : [ 
                {
            "input" : "111",
            "output" : "222",
            "marks" : 1
            },
            {
            "input" : "333",
            "output" : "444",
            "marks" : 2
            }
        ]
    },
        {
        "filename" : "yyy",
        "testCases" : [ 
            {
            "input" : "qqq",# get this 
            "output" : "QQQ",
            "marks" : 1
            },
            {
            "input" : "WWW",
            "output" : "www",
            "marks" : 2
            }
        ]
    }
    ]
}

temp = dict(markings)
print(temp)
temp["filename"]="x"
print(temp)
temp=dict(markings)
print(temp)