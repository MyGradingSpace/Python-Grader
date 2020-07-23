from functions import *
from data_structure import *
import csv
import os


send = dict(responseBody)
send["gradingId"] = "2020-6-CP317T1-A01-5ZMW" # here should be replaced by environmental variable in the future
# send["gradingId"] = getGradingID
path = os.path.join(os.getcwd(), "EXTRACTED")
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
NOS = 0 # number of submission
for index in test["links"]: # test should be replaced by json that requesting from backend in the future
    ID = index["EntityId"]
    #dowload file from link in here
    downloadlink=index["link"]
    download(downloadlink)
    this_results = dict(results)
    this_results["EntityId"] = ID
    this_results["markings"]=[]
    for x in test["configuration"]:
        this_marking= dict(markings)
        this_marking["testResult"]=[]
        this_marking["filename"] = x["filename"]
        this_marking = Run(x,this_marking)
        add_markings(this_marking,this_results)
    NOS+=1 
    add_results(this_results,send)
    
send["numOfSubmissions"] = NOS
print(json.dumps(send, indent=4))
