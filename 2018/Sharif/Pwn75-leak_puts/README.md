---
layout: post
title: "Sharif
date: 3 Février 2018
comments: true
categories: wu
auteur: jambon69
---
```
 ===== INFOS ===== 
Filename                 vuln4
File format              ELF32
Architecture             x86
Endianess                little endian

NX bit                   enabled
Relro                    disabled
PIE                      disabled

```

Le binaire nous demande de trouver nous même l'addresse de puts, avec un read sur stdin juste après.

On va donc générer une première ropchain qui va leak l'addresse de puts et puis rejump sur le main.
Une fois l'addresse de puts obtenue, on peut récupérer l'addresse de system (sachant que la libc utilisée nous est fournie).

Il reste plus qu'à envoyer une deuxième ropchaine qui va exéctuer /bin/sh, et le tour est joué
