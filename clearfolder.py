import shutil
import os

cwd = os.getcwd()
cwd = os.path.join(cwd , "testing_folder")

print(cwd)
try :
    shutil.rmtree(cwd)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))