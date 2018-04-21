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
Filename                 pwnescu
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x9f0
Loadables segments       2
Sections                 29

NX bit                   enabled
SSP                      enabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      enabled
```
La fonction chance se présente comme suit:

void chance(char *p){
        char buf[4096];
        int readcount = read(0, buf, 4095);
        if (readcount < 10) {
                puts("Come on.... seriously?");
                exit(-1);
        }
        validate(buf, readcount);

        if (memcmp(buf, p, 100) == 0 ){
                puts("You win!");
                system("cat /home/`whoami`/flag");
                exit(0);
        } else {
                puts("Guess again!");
        }
}


Donc on peut se contenter de lui passer une chaine de 11 caractères.
Seule cette chaine est testée pour les majuscules. Or d'une part le programme
ne met pas de 0 final à la fin, d'autre part, en mémoire subsite sur la pile
au même endroit où est enregistré le hash calculé le hash obtenu par le
programme.

Il suffit donc de récupérer le seed donné par le programme au début, de calculer
les différents hash et d'envoyer les 11 premiers caractères (sans linefeed
derrière). À un moment il n'y aura pas de majuscule dans ces caractères et on
passera le test.


Bizarrement, ça ne marche pas à tous les coups mais bon...

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

You win!
timctf{a64447f8c8c8bc638ed56a9fdfd7d33c8c760359}

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

