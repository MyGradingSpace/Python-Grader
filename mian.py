from functions import *
import csv

f1=open("arguments.txt","r")

f2=runC(f1,"")
f3=open("answer.txt","r")

output = createOutput(f3,f2)

response = createResponse(output)

response.close()
output.close()
f3.close()
f2.close()
f1.close()




