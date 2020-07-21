import urllib.request
import os

cwd = os.getcwd()
cwd = cwd + "\demo.txt"
print(cwd)
url="https://github.com/fleiray/Fangjian/files/4951342/command.txt"
urllib.request.urlretrieve(url,cwd)