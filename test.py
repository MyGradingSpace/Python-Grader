from data_structure import *
from functions import *
# test={
#     "gradingId" : "",
#     "configuration" : [ 
        
#         {
#         "filename" : "xxx",
#         "testCases" : [ 
#                 {
#             "input" : "111",
#             "output" : "222",
#             "marks" : 1
#             },
#             {
#             "input" : "333",
#             "output" : "444",
#             "marks" : 2
#             }
#         ]
#     },
#         {
#         "filename" : "yyy",
#         "testCases" : [ 
#             {
#             "input" : "qqq",# get this 
#             "output" : "QQQ",
#             "marks" : 1
#             },
#             {
#             "input" : "WWW",
#             "output" : "www",
#             "marks" : 2
#             }
#         ]
#     }
#     ]
# }
# import os
# import shutil
# cwd = os.getcwd()
    
# folder = os.path.join(cwd,'EXTRACTED')

# for the_file in os.listdir(folder):
#     file_path = os.path.join(folder, the_file)
#     try:
#         if os.path.isfile(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print(e)
# if cwd.endswith("EXTRACTED"):
#     folder = cwd
# else:
#     folder = os.path.join(cwd,'EXTRACTED')
# print(folder)
# try:
#     os.rmdir(folder)
# except OSError as e:
#     print("Error: %s : %s" % (folder, e.strerror))
send = dict(responseBody)
send["gradingId"] = "2020-6-haoquan-dropbox-z229" # here should be replaced by environmental variable in the future
# send["gradingId"] = getGradingID()
r = receiveData(send["gradingId"],"oursecret").json()
data=json.loads(r)
print(data)

    
