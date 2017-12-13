#!/usr/bin/python
from pwn import *
p=remote('neverending.tuctf.com' ,12345)

print p.recvuntil("text:")

while(1):
    p.sendline("ABCDEF")
    b= p.recvuntil("?\n:")
    print b
    b=b[b.index("encrypted is ")+len("encrypted is "):]
    print "ABCDEF","->",b
    delta=ord(b[0])-ord("A")
    b=b[b.index("What is ")+len("What is "):]
    b=b[:b.index(" decrypted?")]
    c=""
    for i in b:
        c=c+chr((ord(i)-delta-32+95) % 95+32)
    print "-->",c
    p.sendline(c)
    print p.recv(1000)
    

print p.recvuntil("text:")
p.sendline("ABCDEF")
b= p.recvuntil("?\n:")
print b
b=b[b.index("encrypted is ")+len("encrypted is "):]

print "ABCDEF","->",b
delta=ord(b[0])-ord("A")
b=b[b.index("What is ")+len("What is "):]
b=b[:b.index(" decrypted?")]
c=""
for i in b:
    c=c+chr((ord(i)-delta-32+95) % 95+32)
print "-->",c
p.sendline(c)

print p.recvall(1)
exit(0)
