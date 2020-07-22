import urllib.request
import os
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
# cwd = os.getcwd()
# cwd = cwd + "\demo.zip"


zipurl = 'https://wlutest.desire2learn.com/d2l/api/le/1.34/219419/dropbox/folders/54721/submissions/1542824/files/2675649?x_t=1595381659&x_a=0tBPhBMpv-WkSV8O_oO5Gw&x_c=1drAAGAyRiriC8ce14q8aLk_HI6bLMLXvUR1v8ZcvhI&x_b=lSj3-aOMLSfTGJcUkossnd&x_d=cA9XVjnKD5RlMnWsgWFwQPAoi_fvPbA3eahMEXaLwc8'
# with urlopen(zipurl,timeout=5) as zipresp:
#     with ZipFile(BytesIO(zipresp.read())) as zfile:
#         zfile.extractall('extracted_forlder')
zipresp = urlopen(zipurl,timeout=5)
zfile = ZipFile(BytesIO(zipresp.read()))
zfile.extractall('extracted_folder')

zfile.close()
