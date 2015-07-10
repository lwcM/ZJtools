# by lwc
import requests
import sys
import time

username = 'pcsh710742'
session = ''

problemID = sys.argv[1]

payload = {'problemid':problemID,'account':username}
cookies = {'JSESSIONID':session}
r = requests.get('http://zerojudge.tw/Submissions', cookies=cookies, params=payload)

rtn = r.text
qq = rtn.find('<a href="#" class="acstyle">AC</a>')
if qq == -1:
    print 'not found'
    sys.exit(1)
ss = 'readonly="readonly">'
rtn = rtn[rtn.find('readonly="readonly">'):]
rtn = rtn[len(ss): rtn.find('</textarea>')]
print rtn
