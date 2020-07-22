from functions import *
from data_structure import *
import csv


send = dict(responseBody)
send["gradingId"] = "2020-6-CP317T1-A01-5ZMW" # here should be replaced by environmental variable in the future

for index in test["links"]:
    # print(index)
    ID = index["EntityId"]
    #dowload file from link in here
    this_results = dict(results)
    this_results["EntityId"] = ID
    this_results["markings"]=[]
    for x in test["configuration"]:
        this_marking= dict(markings)
        this_marking["testResult"]=[]
        this_marking["filename"] = x["filename"]
        this_marking = Run(x,this_marking)
        add_markings(this_marking,this_results)
      

    add_results(this_results,send)

print(json.dumps(send, indent=4))


# totalAnswer = []
# for x in test["configuration"]:
#     answer={"filename" : "", "output" : []}
#     filename = x["filename"]
#     answer["filename"] = filename
#     for y in x["testCases"]:
#         output = y["output"]
#         answer["output"].append(output)
#     totalAnswer.append(answer)
# print(totalAnswer)