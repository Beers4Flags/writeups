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
Filename                 heaphop
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x400780
Loadables segments       3
Sections                 28

NX bit                   enabled
SSP                      enabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled
```
La méthode utlisée est celle de la corruption du tcache vue que la libc
est une 2.26 avec donc un cache. On utilise pour ça l'uaf possible puisque le
pointeur est disponible après la libération du bloc.
On alloue un bloc, on le libère, on écrit au début du bloc l'adresse de la got
de la fonction free, on alloue un bloc (le cache est empoisonné) on réalloue
un bloc qui pointe vers la got d'free. On lit cette adresse ce qui donne 
l'adresse de la libc. On la remplace par celle de system. On alloue enfin
un bloc dans lequel on écrit /bin/sh et on libère ce bloc. On obtient un
sehll.