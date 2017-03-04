**Crypto - 100pts**


Le challenge était sur un site web.
Celui-ci nous proposait d'uploader deux fichiers.

Nous créons deux fichiers vide :

```BASH
touch t.txt
touch t2.txt
```

Le site nous redirige sur une page contenant l'information suivante :

```BASH
if sha1[0] == sha1[1] and md5[0] != md5[1]: get flag # ;)
```

Nous avons donc ici une collision sha 1 qui colle pafaitement avec l'actualité du moment.

Notre premier essaye à été d'uploader les deux pdf fournit dans les recherches de collision SHA1 de Google. Ils ont la particularité d'avoir la même somme sha1.

[Fichier 1  : Collision SHA1 par google ](../100/file/shattered-1.pdf)

[Fichier 2  : Collision SHA1 par google ](../100/file/shattered-1.pdf)


Retour du site de challenge => Too Easy.

Nous avons utilisé ce site https://alf.nu/SHA1 pour construire notre collision.

Les prérequis sont deux jpg < 64Ko

![Alt](img/right.jpg "Image 1")

![Alt](img/top.jpg "Image 2")

Le site nous renvoie deux pdf :

[Fichier 1  : Collision SHA1 par Beers4Flags ](../100/file/a.pdf)

[Fichier 2  : Collision SHA1 par Beers4Flags ](../100/file/b.pdf)

Nous verifions que nos deux pdf ont bien la même somme SHA1

```BASH
sha1sum a.pdf 
9895a12be3429d4ca69835aad36527664ed952e5  a.pdf

sha1sum b.pdf
9895a12be3429d4ca69835aad36527664ed952e5  b.pdf
                  
```

Nous les uplodons sur le site et flag !



THCon{ST0P_US1nG_Th0S3_l4m3_H4SH_FuNCTIONz} 


By team Beers4Flags


```
 ________
|        |
|  #BFF  |
|________|
   _.._,_|,_
  (      |   )
   ]~,"-.-~~[
 .=] Beers ([
 | ])  4   ([
 '=]) Flags [
   |:: '    |
    ~~----~~
```
