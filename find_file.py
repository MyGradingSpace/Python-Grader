import os
import subprocess
print("start")
for (subdir, dirs, files) in os.walk('/CP493-Grader',topdown=True):
    print(subdir)
    print(dirs)
    print(files)