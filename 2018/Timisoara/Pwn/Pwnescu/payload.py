#!/usr/bin/python

# encoding: utf-8
from  pwn import *
import time
import sys
import os
#binaire='heaphop'
TIME=0.02
if (len(sys.argv)>1):
#    elf=ELF(binaire)
#    libc=ELF('libc.so.6')
    host='localhost'
    port=59994
else:
#    elf=ELF(binaire)
#    libc=ELF('libc.so.6')
    host='89.38.210.128'
    port=1337

p=remote(host,port)
b=p.recvuntil("!\n")
print b
sseed=b[b.index("is ")+3:b.index("\n")]
seed=int(sseed,16)
print sseed
os.system("./rand "+sseed+" > resultat")
f=open("resultat","r")
l=f.readline()
print p.recvuntil("!\n")
while(len(l)>0):
    print l
    p.send(l[0:11])
    print p.recv("1024")
    l=f.readline()
f.close()

