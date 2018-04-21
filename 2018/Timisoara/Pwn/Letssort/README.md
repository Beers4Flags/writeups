---
layout: post
title: "Timisoara
date: 20 Avril 2018
comments: true
categories: wu
auteur: françois
---
```
 ===== INFOS ===== 
Filename                 letssort
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0xa40
Loadables segments       2
Sections                 27

NX bit                   enabled
SSP                      enabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      enabled
```

Il y a tout d'abord un gros travail de reverse dans ce programme.
* Il prend une chaine de caractère s=[c1,.....,cn] e longueur n
* Il fait une association

ci <-> di = [c(i+1).....c(n)c(1)...c(i-1)]

* Il trie les di, qui donnent une chaine d(i1),d(i2),...,d(in)
* Il est donc relativement facile d'obtenir un classement final voulu aux premières lettres près.

La chaine 

"}a Al Bl Cy D  EL FO GV HE I  Js Ko LR Mt Ni On Pg Q  RA SL Tg Uo VR Wi Xt Yh ZM [s \! ]I ^  _R `e a\x00}}}}}}}}}}}}}}}}}}}}}...." 

permet d'obtenir en sortie

"DIQ^ally LOVE soRting ALgoRithMs!I Re\R    H     ]  ES Z  ..."

On peut enfin noter que si on envoit une chaine terminée par 0, ce 0 n'est pas
mis dans le buffer et le tri ne sefait que sur les lettres du début.
Ainsi pour avoir GLOP, il suffit d'envoyer

"PPPP\x00" puis "OOO\x00" puis "LL\x00" puis "G\x00"

J'ai préféré envoyer la chaine ce dessus puis compltée les 4 premiers caractères
par cette dernière méthode.

Bon, donc on peut sortir du programme.

Un buffer overflow est possible de manière assez grossière mais un canari existe.
Cependant ce canari est facile à retrouver, une fuite a lieu pour des chaines
envoyées de longueur >= 1023.

On procède donc de la façon suivante:

1) Envoi de "a\x00bbbbbbbb[........]bbbbbb" qui permet d'avoir une fuite d'où on
tire le canari et l'adresse de la libc.

2) Envoi de 

"}a Al Bl Cy D  EL FO GV HE I  Js Ko LR Mt Ni On Pg Q  RA SL Tg Uo VR Wi Xt Yh ZM [s \! ]I ^  _R `e a\x00}}}}}}}}}}}}}}}}[...]"+payload 

où le payload est un simple rop réalisant un appel de system avec /bin/sh comme
argument.

3) Envoi de 4 chaines permettant d'obtenir "I Really LOVE soRting ALgoRithMs!"

4) Enjoy du shell

