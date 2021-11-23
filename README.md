# CTF-Scripts
一些简单的scripts，慢慢push

├── README.md
├── compress-zlib.py 
├── ffi-leak.php
├── geneshell.php
├── geneshell2.php
├── misc
│   └── UploadServer.py
├── node-ssrf-split.js node<=8.0 http.get拆分请求构造，对于生成的数据进行encodeUR操作即可
├── port-scan.js
├── serialize.php
├── thread
│   ├── contend.py
│   └── contend2.py
└── transform
    ├── convert2javabytes.py
    ├── encoding.js JS8/16进制/Unicode标准格式转换
    ├── gopher.py
    └── gopherConvert.py


* serialize.php: 对于private/protected属性，序列化后S类型转换(截取phpgcc部分功能)

* geneshell.php: 生成无字母webshell的字母部分，用法见p神：[无字母数字的webshell](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum.html#_4)

* geneshell2.php: 另一种无字母Shell生成函数，无短标签

* compress-zlib.php: file_get_contents生成本地临时文件，使用socket原生套接字改写Http请求&响应包。双线程发送http请求，参考36c3 CTF includer:[includer](https://ljdd520.github.io/2020/01/15/hxp-36c3-ctf-Web-%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95/)

* ffi-leak.php: PHP7.4 FFI extension use to leak data，来源：[@cjm00n](https://cjm00n.top/CTF/tctf-2020-wp.html)

* port-scan.js: JS探测内网主机端口/内网主机

* gopher.py: 生成post的gopher数据报文

* UploadServer.py: 以当前目录，快速启动一个带有文件上传/下载功能代理服务器. Usage: python2 UploadServer.py 8888

* contend.py: threading条件竞争模版，用来竞争php sess文件

* gopherConvert.py: wireshark网卡数据包转gopher数据形式

* convert2javabytes.py: 转字符串为16进制形式，方便java中的命令执行例如：${T(java.lang.Runtime).getRuntime().exec(new String(new byte[]{0x6f,0x70,0x65,0x6e,0x20,0x2d,0x61,0x20,0x43,0x61,0x6c,0x63,0x75,0x6c,0x61,0x74,0x6f,0x72}))}
