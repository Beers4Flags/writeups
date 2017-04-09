**Misc - Something Strange - 2500**

Un dossier compressé nous est fournis dans l'énoncé du challenge.
Dedans des fichiers :

```BASH
fileA  fileD  fileF  fileH  fileJ  fileM  fileP  fileU  fileW  fileY
fileB  fileE  fileG  fileI  fileL  fileO  fileR  fileV  fileX
```


Résolution :
On constate une différence sur les dates de modification des fichiers :

```BASH
stat fileA fileB

  Fichier : « fileA »
   Taille : 7         	Blocs : 8          Blocs d'E/S : 4096   fichier
Périphérique : fe01h/65025d	Inœud : 8389338     Liens : 1
Accès : (0644/-rw-r--r--)  UID : ( 1000/ ark1nar)   GID : ( 1000/ ark1nar)
 Accès : 2017-04-09 20:13:10.945251310 +0200
Modif. : 2017-04-02 14:44:32.000000000 +0200
Changt : 2017-04-07 22:24:01.197520050 +0200
  Créé : -
  Fichier : « fileB »
   Taille : 17        	Blocs : 8          Blocs d'E/S : 4096   fichier
Périphérique : fe01h/65025d	Inœud : 8389339     Liens : 1
Accès : (0644/-rw-r--r--)  UID : ( 1000/ ark1nar)   GID : ( 1000/ ark1nar)
 Accès : 2017-04-09 20:13:10.945251310 +0200
Modif. : 2017-04-02 14:39:32.000000000 +0200
Changt : 2017-04-07 22:24:01.197520050 +0200
  Créé : -
```

On les stocke dans un fichier en les triant par ordre croissant :


```BASH

cat $(ls file* --sort=time | tac) > solve

```

Dans le fichier solve on met les "obase" à la fin du fichier et on supprime le "quit".

Notre fichier est le suivant :
```BASH
j=(7^2+4)

x=84

m=(20+32)
x=x-4

d=123

p=100

b=100+(4 && 10)

i=95

u=(81+72)-m
x=sqrt(x)

l=6*((1+1)*7)

if (u == 101 ) { w = 52 }
x=x*2

a=w+m

for(h=0;h<16;h++) {y+=7}

y=y+6

e=95

g=w-1

f=(p-x-1)

o=p+x

r=p+(w/2)-(4 && 10)

obase=x;d
obase=x;f
obase=x;w
obase=x;y
obase=x;u
obase=x;i
obase=x;o
obase=x;a
obase=x;g
obase=x;e
obase=x;p
obase=x;m
obase=x;l
obase=x;b
obase=x;j
obase=x;r

```
On affiche le flag :

```BASH
cat solve| bc | xxd -r -p
{S4ve_th3_d4Te5}
```


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