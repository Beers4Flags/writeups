---
layout: post
title: "CSAW CTF"
date: 18 Septembre 2017
comments: true
categories: wu
---
 ===== INFOS ===== 
Filename                 pilot
File format              ELF64
Architecture             x86-64
Endianess                little endian
Entry point              0x4008b0
Loadables segments       2
Sections                 31

NX bit                   disabled
SSP                      disabled
Relro                    partial
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled

Le binaire est un binaire avec un buffer overflow simple, la pile est donnée et
elle est exécutable. On peut juste mettre un nombre limité d'octets. On commence
donc par le shellcode qui devra commencer par diminuer $rsp afin de ne pas
s'écraser en empilant des adresses.