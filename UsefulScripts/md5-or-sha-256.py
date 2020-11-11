import hashlib
import string

f = open("FLAG.txt")
buffer = f.read()
hashlist = buffer.split(" ")
flag = ""
for h in hashlist:
    for c in string.printable:
        if hashlib.sha256(c).hexdigest() == h:
            flag += c
            break
        elif hashlib.md5(c).hexdigest() == h:
            flag += c
            break
    else:
        break

print(flag)
open("flag", "wb").write(flag)
