import csv
import os
import subprocess

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

def createOutput(file1, file2):
    i=getCaseNumber(file1)
    n=0
    answer = getContent(file1)
    output = getContent(file2)
    file1.seek(0)
    file2.seek(0)
    with open('output.csv', 'w', newline='') as file:
        fnames = ["Case Number", "Output","Expect Output", "Result"]
        writer = csv.DictWriter(file, fieldnames=fnames) 
        writer.writeheader()
        for n in range(i):
            line1 = file1.readline()
            line2 = file2.readline()
            b = result(line1, line2)
            c= getCaseSequence(line1)          
            writer.writerow({"Case Number" : "Case"+c, "Output" : output[n], "Expect Output" : answer[n], "Result" : b})

    return file


