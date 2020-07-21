import urllib.request
import os
from zipfile import ZipFile


cwd = os.getcwd()
cwd = cwd + "\demo.zip"
print(cwd)
url="https://github.com/fleiray/Fangjian/files/4954930/command.zip"
urllib.request.urlretrieve(url,cwd)

with ZipFile("demo.zip","r") as zipobj:
    zipobj.extractall("extracted_forlder")