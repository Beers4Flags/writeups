**RSA_16M - CRYPTO -125**

L'énoncé nous fournit un fichier contenant :

1. un modulo d'une taille extrème
2. un exposant : 65537
3. un cipher d'une taille extrème

__Résolution :__

On commence par isoler le cipher dans un fichier seul :

```
0x3f33e5d55269698e9cc81d355d4420330e9e8fbfa6c4ae88b728e0e94de47604a8c67270099a6a36e1795a3f97fd0a9e3be648c8f38652abb47a4bde[...]

```

On charge le fichier dans sagemath et on le dechiffre :

```PYTHON
sage: file=open("cipher","r")
sage: cipher_hex=file.read()
sage: cipher_dec=int(cipher_hex,16)
sage: flag=pow(cipher_dec,1/e)
sage: flag
30156321943599743278455918182580886589695285093075236154009535613
sage: hex(30156321943599743278455918182580886589695285093075236154009535613).dec
....: ode("hex")
'INSA{(I)NSA_W0uld_bE_pr0uD}'
```

Le modulo étant trop grand il n'est pas pris en compte lors du chiffrement.


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