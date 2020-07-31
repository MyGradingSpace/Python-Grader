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

def sendResult(fdata,secretKey):
    # fdata =open("send.json","rb")
    # r = requests.put('https://pretty-printed-request-bin.herokuapp.com/1kvflzr1',data=fdata, headers={"key":"oursecret","Content-Type":"application/json"}, timeout=5)
    r = requests.put('http://localhost:5000/grading',data=fdata, headers={"key": secretKey,"Content-Type":"application/json"}, timeout=10)
    
    return 

def receiveData(gradingID,secretKey):

    r = requests.get('http://localhost:5000/joblinks',params={"gradingId" : gradingID},headers={"key":secretKey}, timeout=10)

    return r

def getGradingID():
    gradingID = os.environ['GRADINGID']
    return gradingID

def download(zipurl):
    clearFolder()
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
        os.umask(0)
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
        os.umask(0)
        os.rmdir(folder)
    except OSError as e:
        print("Error: %s : %s" % (folder, e.strerror))
    return