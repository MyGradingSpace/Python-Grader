import csv
import os
import subprocess
from data_structure import testResult,markings,results,responseBody
from data_structure import add_testResult,add_markings,add_results
import fnmatch
import time
from subprocess import STDOUT, check_output
from threading import Timer
import json
import requests
import urllib.request
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import shutil

# def getCaseSequence(line):
#     CaseSequence = line[4]
#     return CaseSequence


# def getCaseNumber(file):
#     caseNumber = 0
#     file.seek(0)
#     for line in file:
#         caseNumber += 1
#     return caseNumber

# # comparing the single line between input and sample output
# def comparsion(line1, line2):
#     b = False
#     if line1 != line2:
#         b=False
#     else:
#         b=True
#     return b

# def marking(submission, answer):

#     submission.seek(0)
#     answer.seek(0)
#     totalCase = getCaseNumber(answer)

#     correctCase = 0

#     for line1 in answer:
#         for line2 in submission:
#             b = comparsion(line1,line2)
#             if b == True:
#                 correctCase += 1
    
#     incorrectCase = totalCase - correctCase

#     return incorrectCase, correctCase

# def result(line1, line2):
#     b = comparsion(line1, line2)
#     if b == True:
#         result = "Correct"
#     else:
#         result = "Incorect"
#     return result

# # get content for each case
# def getContent(file1):
#     file1.seek(0)
#     Content=[]
#     for line1 in file1: 
#         Content.append(line1.strip())
#     return Content

# runing one task(filename) for all testing cases only for single student 
# EXEname=""
def Run(args,markings): #args is receiveBody[configuration] dictionary, filename is the one of keys in configuration
    filename = args["filename"]
    dirpath = os.getcwd()
    if dirpath.endswith("EXTRACTED"):
        p = dirpath
        # print(True)
    else:
        p = dirpath + '/EXTRACTED'
    
    os.chdir(p)
    
    # global EXEname
    for file in os.listdir(p):
        if fnmatch.fnmatch(file,filename):
            EXEname = file[:-2] # name of .exe
    # EXEname += ".exe"
    command = "gcc -o " + EXEname + " " + filename
    os.system(command)
    temp_testResult = dict(testResult)
    for y in args["testCases"]:
        para = y["input"]
        ans = y["output"]
        mark = y["marks"]
        command = "./" + EXEname 
        output = check_output([command]+para.split(),stderr=STDOUT,timeout=5.5)
        output = str(output)
        output.strip("\n")
        output.strip("\r")
        output=output[2:-1]
        temp_testResult["output"] = output
        temp_testResult["expectOutput"] = ans
        if output == ans:
           temp_testResult["match"] = True
           temp_testResult["marks"] = mark
        else:
            temp_testResult["match"] = False
            temp_testResult["marks"] = 0
        markings["marked"]=True
        add_testResult(temp_testResult,markings)
        temp_testResult = dict(testResult)
    
    return markings


# def createResponse(output):
#     # output=open("output.csv","r")
#     gradingID = "2020-6-CP317T1-A01-5ZMW"
#     numberOfSubmission = 1
#     studentID = "3432423"

#     this_responseBody = dict(responseBody)
#     this_results = dict(results)
#     df = pd.read_csv(output, delimiter=',',dtype=str)
#     # df = pd.read_csv(output, delimiter=',')
#     this_responseBody["gradingId"] = gradingID
#     this_responseBody["numOfSubmissions"]=numberOfSubmission
#     # this_results ["studentID"] =studentID
#     this_results["EntityId"] = studentID
#     this_testResult =dict(testResult)
#     this_markings =dict(markings)
#     this_markings["filename"] = "a2q2"
#     this_markings["marked"] = True
    
#     with open("send.json","w+") as json_file:
#         i=0
#         for i in range(len(df.index)):

#             this_testResult["output"] = df["Output"][i]
#             this_testResult["expectOutput"] = df["Expect Output"][i]
#             this_testResult["match"] =bool(df["Result"][i])
#             this_testResult["marks"] = int(df["Marks"][i])

#             add_testResult(this_testResult,this_markings)
#             this_testResult =dict(testResult)
        
#         add_markings(this_markings,this_results)
#         add_results(this_results,this_responseBody)
        
#         json.dump(this_responseBody,json_file,indent=4)
    
#     return json_file

def sendResult(fdata,secretKey):
    # fdata =open("send.json","rb")
    # print(json.dump(fdata))
    # r = requests.put('https://pretty-printed-request-bin.herokuapp.com/1kvflzr1',data=fdata, headers={"key":"oursecret","Content-Type":"application/json"}, timeout=5)
    r = requests.put('http://localhost:5000/grading',data=fdata, headers={"key": secretKey,"Content-Type":"application/json"}, timeout=10)
    
    return 

def receiveData(gradingID,secretKey):

    r = requests.get('http://localhost:5000/joblinks',params={"gradingId" : gradingID},headers={"key":secretKey}, timeout=10)

    return r

def getGradingID():
    gradingID = os.environ['gradingId']
    return gradingID

def download(zipurl):
    clearFolder()
    # cwd = os.getcwd()
    # cwd = cwd + "\demo.zip"
    
    #zipurl = 'https://wlutest.desire2learn.com/d2l/api/le/1.34/219419/dropbox/folders/54721/submissions/1542824/files/2675649?x_t=1595381659&x_a=0tBPhBMpv-WkSV8O_oO5Gw&x_c=1drAAGAyRiriC8ce14q8aLk_HI6bLMLXvUR1v8ZcvhI&x_b=lSj3-aOMLSfTGJcUkossnd&x_d=cA9XVjnKD5RlMnWsgWFwQPAoi_fvPbA3eahMEXaLwc8'
    
    # with urlopen(zipurl,timeout=5) as zipresp:
    #     with ZipFile(BytesIO(zipresp.read())) as zfile:
    #         zfile.extractall('extracted_forlder')
    cwd = os.getcwd()
    if cwd.endswith("EXTRACTED"):
        folder = cwd
    else:
        folder = os.path.join(cwd,'EXTRACTED')
    zipresp = urlopen(zipurl,timeout=5)
    zfile = ZipFile(BytesIO(zipresp.read()))
    zfile.extractall(path=folder)

    zipresp.close()
    zfile.close()
    return

def clearFolder():
    
    cwd = os.getcwd()
    if cwd.endswith("EXTRACTED"):
        folder = cwd
    else:
        folder = os.path.join(cwd,'EXTRACTED')

    if not os.path.exists(folder):
        os.makedirs(folder)

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    if cwd.endswith("EXTRACTED"):
        folder = cwd
    else:
        folder = os.path.join(cwd,'EXTRACTED')
    try:
        os.rmdir(folder)
    except OSError as e:
        print("Error: %s : %s" % (folder, e.strerror))
    return