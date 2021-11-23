# coding: utf-8

result = ""
target = 'open -a Calculator'
for x in target:
    result += hex(ord(x)) + ","
print(result.rstrip(','))
