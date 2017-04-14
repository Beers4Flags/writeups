**Encryption Program Leaked - Crypto - 100**

Enoncé :

```
The encryption program and secret key leaked out!!


key = eglafdsewafslfewamfeopwamfe
encrypt = 5857342f555c2528182b55175e5f543a14540a0617394504380a0e52
```

Les sources : [Cryptographic_program.py](src/Cryptographic_program.py)

__Résolution :__

On commence par analyser ce que font chaque fonctions :

La fonction padd : Elle passe de l ascii à un tableau en decimal et rajoute du padding pour que les deux tableaux fassent la même taille.

```PYTHON

def padd(stirng_v1,string_v2):
    list_stirng_v1,list_stirng_v2 = strint(list(stirng_v1),list(string_v2))
    ex = len(list_stirng_v1)-len(list_stirng_v2)
    if ex >= 0:
        for i in range(ex):
            list_stirng_v2.append(0)
        return list_stirng_v1,list_stirng_v2
    else:
        for i in range(abs(ex)):
            list_stirng_v1.append(0)
        return list_stirng_v1,list_stirng_v2
```


La fonction hex_l : Permet de passer d'un tableau de decimal à une chaine en hexa [97, 97, 0] => 616100

```PYTHON
def hex_l(a):  # 
    a_hex = []
    for i in a:
        a_hex.append("%02x" % i)
    return "".join(a_hex)
```

La fonction encrypt : 

1ère Etape : 

Elle commence par appeler la fonction padd en lui passant deux chaines de caractères :

stringv=base64.b64encode("FIT{}")   #base64 de FIT{}

et la key=key

Nous obtenons ça :
```
stringv=[82, 107, 108, 85, 101, 51, 48, 61]
key=[107, 101, 121, 0, 0, 0, 0, 0]
```

2ème Etape :

stringv[::-1] va inverser les nombres du tableau : [61, 48, 51, 101, 85, 108, 107, 82]

La fonction zip() va faire des tuples de données entre stringv et notre key :
```PYTHON
>>> zip(stringv[::-1],key)
[(61, 107), (48, 101), (51, 121), (101, 0), (85, 0), (108, 0), (107, 0), (82, 0)]
```

Et pour finir on xor chaque élément du tuple avec le deuxième :

61 xor 107 => 86
48 xor 101 => 85
[...]

On retourne tout ce beau monde dans un tableau :

[86, 85, 74, 101, 85, 108, 107, 82]

Puis on ajoute la clé pour faire deux tableaux dans un :

([86, 85, 74, 101, 85, 108, 107, 82], [107, 101, 121, 0, 0, 0, 0, 0])

```PYTHON
def encrypt(flag,key):
    stringv,key = padd(flag,key) #Etape 1
    return [i^j for i,j in zip(stringv[::-1],key)],key  #Etape 2

```

Maintenant il faut faire le processus inverse pour retrouver le flag :

1. Passer le chiffré 5857342f555c2528182b55175e5f543a14540a0617394504380a0e52 en tableau de decimal : [88, 87, 52, 47, 85, 92, 37, 40, 24, 43, 85, 23, 94, 95, 84, 58, 20, 84, 10, 6, 23, 57, 69, 4, 56, 10, 14, 82]
2. Passer la clé eglafdsewafslfewamfeopwamfe en tableau de decimal et lui ajouter le padding pour qu'elle fasse la même taille que le chiffré : [88, 87, 52, 47, 85, 92, 37, 40, 24, 43, 85, 23, 94, 95, 84, 58, 20, 84, 10, 6, 23, 57, 69, 4, 56, 10, 14, 82]
3. Inverser le tableau du chiffré
4. Faire des tuples avec les deux tableaux
5. xorer les tuples entres eux
6. Reinverser le flag et le décoder

Mon code pour faire cela :

```PYTHON
import base64

flag_b64=""
list=[]
key=[101, 103, 108, 97, 102, 100, 115, 101, 119, 97, 102, 115, 108, 102, 101, 119, 97, 109, 102, 101, 111, 112, 119, 97, 109, 102, 101,0]
flag=[88, 87, 52, 47, 85, 92, 37, 40, 24, 43, 85, 23, 94, 95, 84, 58, 20, 84, 10, 6, 23, 57, 69, 4, 56, 10, 14, 82]

revflag=flag[::-1]
kf=zip(flag,key)
print "---------------------- XOR ----------------------------------------"
retkf=[i^j for i,j in kf]
for e in retkf:
	flag_b64+=chr(e)

#print flag_b64[::-1]

print "flag : "+str(base64.b64decode(flag_b64[::-1]))

```

L'avantage du xor est qu'il est reversible c'est grâce à cela que l'on peut récupérer le flag en clair.

```
---------------------- XOR ----------------------------------------
flag : FIT{b1r_n3_vwrh1_75}
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
