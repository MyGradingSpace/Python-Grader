import csv
import os
import subprocess
from data_structure import testResult,markings,results,responseBody
from data_structure import add_testResult,add_markings,add_results
import fnmatch
import time
from subprocess import STDOUT, check_output
from threading import Timer
import pandas as pd
import json


output=open("output.csv","r")
gradingID = "YYYYMM-CP493-a01-ab12"
numberOfSubmission = 1
studentName = "Fangjian Lei"
studentID = "163165490"

this_responseBody = dict(responseBody)
this_results = dict(results)
df = pd.read_csv(output, delimiter=',',dtype=str)
this_responseBody["gradingId"] = gradingID
this_responseBody["numOfSubmissions"]=numberOfSubmission
this_results ["studentID"] =studentID
this_results["EntityId"] = ""
this_testResult =dict(testResult)
this_markings =dict(markings)
this_markings["filename"] = "a2q2"
this_markings["marked"] = True
with open("send.json","w+") as json_file:
    i=0
    for i in range(len(df.index)):
        # print(df["Case Number"][i])
        
        this_testResult["output"] = df["Output"][i]
        this_testResult["expectOutput"] = df["Expect Output"][i]
        this_testResult["match"] =df["Result"][i]
        this_testResult["marks"] = df["Marks"][i]
        # this_markings["testResult"] = this_testResult
        add_testResult(this_testResult,this_markings)
        this_testResult =dict(testResult)
    add_markings(this_markings,this_results)
    add_results(this_results,this_responseBody)
    
    json.dump(this_responseBody,json_file,indent=4)
    
output.close()
json_file.close()

