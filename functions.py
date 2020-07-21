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


def getCaseSequence(line):
    CaseSequence = line[4]
    return CaseSequence


def getCaseNumber(file):
    caseNumber = 0
    file.seek(0)
    for line in file:
        caseNumber += 1
    return caseNumber

# comparing the single line between input and sample output
def comparsion(line1, line2):
    b = False
    if line1 != line2:
        b=False
    else:
        b=True
    return b

def marking(submission, answer):

    submission.seek(0)
    answer.seek(0)
    totalCase = getCaseNumber(answer)

    correctCase = 0

    for line1 in answer:
        for line2 in submission:
            b = comparsion(line1,line2)
            if b == True:
                correctCase += 1
    
    incorrectCase = totalCase - correctCase

    return incorrectCase, correctCase

def result(line1, line2):
    b = comparsion(line1, line2)
    if b == True:
        result = "Correct"
    else:
        result = "Incorect"
    return result

# get content for each case
def getContent(file1):
    file1.seek(0)
    Content=[]
    for line1 in file1: 
        Content.append(line1.strip())
    return Content

def createOutput(file1, file2): #file1 is answer, file2 is submission
    i=getCaseNumber(file1)
    n=0
    answer = getContent(file1)
    output = getContent(file2)
    file1.seek(0)
    file2.seek(0)
    with open('output.csv', 'w+', newline='') as file:
        fnames = ["Case Number", "Output","Expect Output", "Result","Marks"]
        writer = csv.DictWriter(file, fieldnames=fnames) 
        writer.writeheader()
        c=1
        for n in range(i):
            line1 = file1.readline()
            line2 = file2.readline()
            #c= getCaseSequence(line1)
            b = comparsion(line1, line2)        
            if b == True:
                writer.writerow({"Case Number" : "Case" + str(c), "Output" : output[n], "Expect Output" : answer[n], "Result" : b,"Marks" : 1})
            else:
                writer.writerow({"Case Number" : "Case" + str(c), "Output" : output[n], "Expect Output" : answer[n], "Result" : b,"Marks" : 0})
            c=c+1
    
    temp=open(file.name,"r")   
    
    return temp

def runC(args,Cname): # c file name
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.c'):
            filename = file[:-2]
            absolutefile = file
    command = "gcc -o "+filename +" " + absolutefile
    os.system(command)
    n=1
    args.seek(0)
    StuSubs = open("submission.txt","r+")
    for line in args:
        command = filename +" " + line
        output = check_output(command,stderr=STDOUT,timeout=5.5)
        output = str(output)
        output.strip("\n")
        output.strip("\r")
        output=output[2:-1]
        #output = "case"+str(n)+" "+output+"\n" 
        output = output+"\n"
        StuSubs.write(output)
        n=n+1
    return StuSubs

def createResponse(output):
    # output=open("output.csv","r")
    gradingID = "2020-6-CP317T1-A01-5ZMW"
    numberOfSubmission = 1
    studentID = "3432423"

    this_responseBody = dict(responseBody)
    this_results = dict(results)
    df = pd.read_csv(output, delimiter=',',dtype=str)
    # df = pd.read_csv(output, delimiter=',')
    this_responseBody["gradingId"] = gradingID
    this_responseBody["numOfSubmissions"]=numberOfSubmission
    # this_results ["studentID"] =studentID
    this_results["EntityId"] = studentID
    this_testResult =dict(testResult)
    this_markings =dict(markings)
    this_markings["filename"] = "a2q2"
    this_markings["marked"] = True
    
    with open("send.json","w+") as json_file:
        i=0
        for i in range(len(df.index)):

            this_testResult["output"] = df["Output"][i]
            this_testResult["expectOutput"] = df["Expect Output"][i]
            this_testResult["match"] =bool(df["Result"][i])
            this_testResult["marks"] = int(df["Marks"][i])

            add_testResult(this_testResult,this_markings)
            this_testResult =dict(testResult)
        
        add_markings(this_markings,this_results)
        add_results(this_results,this_responseBody)
        
        json.dump(this_responseBody,json_file,indent=4)
    
    return json_file
