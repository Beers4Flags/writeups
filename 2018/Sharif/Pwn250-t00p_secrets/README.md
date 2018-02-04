---
layout: post
title: "Sharif
date: 3 Février 2018
comments: true
categories: wu
auteur: françois
---
```
 ===== INFOS ===== 
Filename                 t00p_secrets
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x4008f0
Loadables segments       2
Sections                 27

NX bit                   enabled
SSP                      enabled
Relro                    full
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled
```
Le binaire présent un off-by-one permettant de modifier le champs previous-use
d'un chunk. On va donc pouvoir faire un safe unlink en faisant
[fake chunk][0...0][taille chunk]|ecrituee d'un 0 sur la longueur d'un bloc
de taille 0x200, le bloc précédent sera marqué comme libre.

On libère le bloc et cela crée une entrée (numero 4) dans la liste des secrets
permettant de modifier une autre entrée (la numéro 1).

On affiche alors la got de puts, on en déduit la libc (xenial 2.23), puis
on met __free_hook vers 6 et on détruit le secret 0 contenant /bin/sh.

On a alors un shell.
