* l3console
Ce programme présente une faille de type format au niveau de la commande e
1) On commence par faire boucler le programme en remplaçant l'entrée got de exit par main.

2) En suite on récupère de manière classique l'entrée got de printf, fgets, puts, strok afin d'identifier de façon certaine la libc

3) On remplace l'entrée got de strok par celle de system et on déclenche la vulnérabilité.


* l3matrix:
matrixnécessite tout d'abord un module python pour convertir un flottant en chaine de 4 caractères (pwnfloat.c joint)
La vyulnérabilité vient du fait qu'un élément est adressé par i * nblignes + j où i est le numéro de ligne et j celui de la colonne. Cela est faux, il aurait fallu faire i * nbcolonnes + j. Cela permet en tout cas d'écraser un élement au delà du bloc et donc entre autre le pointeur vers une matrice. On peut lire et écrire n'importe où. Dès ce moment on récupère l'entrée got de printf et on remplace l'entrée got de scanf par celle de system.


* l3chat:
chat-logger est plus subtil, en fait lors de l'update on peut écraser la longueur du bloc suivant. Cela se fait par une séquence d'édition de messages (voir sortie villoc chat.html ). Dès cet instant on peut faire fuiter l'entrée got de printf et identifier la libc puis remplacer strchr par system. Les réglages ne sont pas simples.

* l4flag est amusant, une faille format pas forcement simple que l'on exploite de la façon suivante: L'entrée 17 de la pile pointe vers l'entrée 53 qui est un pointeur vers la pile. On peut donc
1) localiser la pile puisqu'on connait l'adresse de l'entrée 53 de cette pile
2) En modifiant la partie basse de cette entrée à l'aide d'un format %17$hn, on peut faire pointer 53 faire ce qu'on veut sur la pile et donc faire pointer 55 et 56 où on veut. Par ce rebond on peut lire et écrire ce qu'on veut en mémoire.
3) La libc peut se localiser comme cela ou plus simplement en notant que l'entrée 2 de la pile (%2$08x) donne l'adresse de __IO_2_1_stdin dans la libc.
4) On exploite tout ça en remplaçant l'entrée got de strchr par celle de system.
