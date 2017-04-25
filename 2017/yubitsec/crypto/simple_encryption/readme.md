**Simple Encryption - Crypto - 175**

Enoncé :

```
Deux fichiers sont mis à notre disposition :

1 - Un chiffré
2 - Le script python pour chiffrer
```
[Sources](src/)

__Résolution :__

Le script de "chiffrement" xor chaque caractère (passé en décimal) avec le nombre 62.

Il suffit de faire de même pour retrouver le flag en clair.


```PYTHON
encrypted=[103,107,124,119,106,109,123,125,69,73,91,82,82,97,89,76,91,95,74,67]
char=""
for nb in encrypted:
	char+=chr(nb^62)
print char
```
YUBITSEC{well_great}

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
