**RSA 2 - Crypto - 350**

Enoncé :

```
Can you decrypt these ciphertexts ?
```
[Sources](src/)

__Résolution :__

On récupère les informations contenues dans la clé publique :

```BASH
openssl rsa -in pubkey.pem -pubin -text -modulus
```
```
Public-Key: (7470 bit)
Modulus:
    3f:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
[...]
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:01
Exponent: 65537 (0x10001)
Modulus=3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[...]0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
-----BEGIN PUBLIC KEY-----
MIIDxzANBgkqhkiG9w0BAQEFAAOCA7QAMIIDrwKCA6Y/////////////////////
////////////////////////////////////////////////////////////////
[...]
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAABAgMBAAE=
-----END PUBLIC KEY-----
```

On passe le modulo de hexa à int :
```
sage : n=int("mon_modulo_en_hexa",16)
```

La longueur du modulo est trop élevé pour être factorisé directement

On va voir si il a déjà été factorisé sur [factordb](http://factordb.com/)

=> full factorized : on a les deux facteurs p & q
     
On recréé les clé publique avec rsatool :
```BASH
python rsatool.py -p mon_p -q mon_q -f PEM -o privkey.pem
```

On déchiffre : 

```BASH
openssl rsautl -decrypt -inkey privkey.pem -in cipher.txt
```  

YUBITSEC{G00D_J0B_BRO_Y0U_MUST_KN0W_H0W_D03S_1T_W0RKS}

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
