import os
import subprocess
import fnmatch
import time
from subprocess import STDOUT, check_output
from threading import Timer

args = open("arguments.txt","r")
outF = open("submission.txt","w")

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.c'):
        filename = file[:-2]
        #print(file)
        #print(filename)
        absolutefile = file

command = "gcc -o "+filename +" " + absolutefile
os.system(command)
#print(command)
n=1
outF.seek(0)
args.seek(0)
# kill = lambda process: process.kill()
for line in args:
    command = filename +" " + line
    #os.system(command)
    output = check_output(command,stderr=STDOUT,timeout=5.5)
    #output = subprocess.getoutput(command)
    output = str(output)
    output.strip("\n")
    output.strip("\r")
    output=output[2:-1]
    output = "case"+str(n)+" "+output+"\n" 
    outF.write(output)

    # command=filename+" "+line
    # output = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # my_timer = Timer(5.0,kill,[output])
    # try:
    #     my_timer.start()
    #     stdout,stderr = output.communicate()
    # finally:
    #     my_timer.cancel()
    # finalOutput = str(stdout)[2:-1]
    # finalOutput.rstrip("\r\n")
 
    # finalOutput = "case"+str(n)+" "+finalOutput+"\n"
    # outF.write(finalOutput)
    n=n+1

args.close()
outF.close()