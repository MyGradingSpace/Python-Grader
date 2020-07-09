from functions import *
import csv

f1=open("answer.txt","r")
f2=open("submission.txt","r")

output = createOutput(f1,f2)

f1.close()
f2.close()
output.close()



