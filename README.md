# CTF-Scripts
一些简单的scripts，慢慢push


* encoding.js: JS8/16进制/Unicode标准格式转换

* serialize.php: 对于private/protected属性，序列化后S类型转换(截取phpgcc部分功能)

* geneshell.php: 生成无字母webshell的字母部分，用法见p神：[无字母数字的webshell](https://www.leavesongs.com/PENETRATION/webshell-without-alphanum.html#_4)

* compress-zlib.php: file_get_contents生成本地临时文件，使用socket原生套接字改写Http请求&响应包。双线程发送http请求，参考36c3 CTF includer:[includer](https://ljdd520.github.io/2020/01/15/hxp-36c3-ctf-Web-%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95/)

* ffi-leak.php: PHP7.4 FFI extension use to leak data，来源：[@cjm00n](https://cjm00n.top/CTF/tctf-2020-wp.html)
