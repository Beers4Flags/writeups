---
layout: post
title: CodegateCTF
date: 3 Février 2018
comments: true
categories: wu
auteur: jambon69
---
```

## RedVelvet

Le binaire n'est pas strippé, donc le reverse de base est assez facile.

On se retrouve face à 15 fonctions qui font des opérations sur les différents charactères du flag.
Qui dit conditions dit z3, on ressort donc le bon vieil algorithm solver de Microsoft

A la fin on a 4 flags qui satisfont les conditions, on les essaye tous.

Le bon est finalement `What_You_Wanna_Be?:)_la_la`

Bon ici j'ai utilisé un BitVec par charactère puisqu'on utilise des opérations bit à bit qui ne sont pas supportés par les Int de z3. C'est un peu crade, mais ça fait le boulot.
