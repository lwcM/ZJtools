# by lwc
import requests
import sys
import time

session = ''

filename = sys.argv[1]
problemID = filename[0:4]
f = open(filename)
code = ''
for line in f:
    code += line

payload = {'action':'SubmitCode','problemid':problemID,'language':'CPP','code':code}
cookies = {'JSESSIONID':session}
r = requests.post('http://zerojudge.tw/Solution.api', cookies=cookies, params=payload)

if r.content == '{"uri":"/Submissions"}':
    print 'Submission OK'
else:
    print 'Fail to submit'
    sys.exit(0)

time.sleep(3)
r = requests.get('http://zerojudge.tw/Submissions', cookies=cookies)
rtn = r.text
rtn = rtn[rtn.find('lwcQQ'):]
ss = '<a href="#" class="acstyle">'
rtn = rtn[rtn.find(ss):]
rtn = rtn[len(ss):rtn.find('</a>')]
print 'Result: ' + rtn
