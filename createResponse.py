import csv
import os
import subprocess
from data_structure import submission,grades,results,responseBody
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

i=0
df = pd.read_csv(output, delimiter=',')
# print(len(df.index))

with open("send.txt","w+") as json_file:
    this_submission = dict(submission)
    this_grades = dict(grades)
    this_responseBody["gradingId"] = gradingID
    this_responseBody["numOfSubmissions"]=numberOfSubmission
    this_responseBody["results"]=this_results
    json.dump(this_responseBody,json_file)
    for i in range(len(df.index)):
        this_submission = dict(submission)
        this_grades = dict(grades)
        this_submission["output"] = df["Output"][i]
        this_submission["expectOutput"] = df["Expect Output"][i]
        this_submission["match"] =df["Result"][i]
        this_grades["taskname"] = "a2q2"
        this_grades["testCase"] = df["Case Number"][i]
        this_grades["CaseNumber"] = i+1
        this_grades["submission"] = this_submission
    this_results["studentName"] = studentName
    this_results ["stduentId"] =studentID
    this_results["fileId"] = ""
    this_results["fileName"] = ""
    this_results["grades"]=this_grades

    # this_responseBody["gradingId"] = gradingID
    # this_responseBody["numberOfSubmission"]=numberOfSubmission
    # this_responseBody["results"]=this_results
    # json.dump(this_responseBody,json_file)

output.close()
json_file.close()

def add_grades(grades,results):
    results["grades"].append(grades)
    return