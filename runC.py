import os
import subprocess

args = open("arguments.txt","r")
outF = open("submission.txt","w")

#/CP493-Grader

n=1
for line in args:
    command = "a2q2 " + line
    os.system(command)
    output = subprocess.getoutput(command)
    output = str(output)
    output.strip("\n")
    output.strip("\r")
    output = "case"+str(n)+" "+output+"\n"
    outF.write(output)
    n=n+1
args.close()
outF.close()