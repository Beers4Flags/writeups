**Crypto - RSA 2 - 80pts**

Fournit dans l'énoncé du challenge :

```BASH
The first thing that  some more RSA : This time, there's no P and Q .. this : 

n: 266965481915457805187702917726550329693157
e: 65537
c: 78670065603555615007383828728708393504251
```

Nous avons recontruit la clé privé avec sagemath pour déchiffrer "c" :

```PYTHON
sage: n=567093316760996114722721565371530382210929
sage: e=65537
sage: c=38553683267453753948267180793639101810598
```

On factorise le modulo "n" :

```PYTHON
sage: factor(n)
680196774012131697983 * 833719503572478986063
sage: p=680196774012131697983
sage: q=833719503572478986063
```

On va reconstruire "d" qui est l'exposant privé.

```PYTHON
sage: phi=(p-1)*(q-1)
sage: d=inverse_mod(e,phi)
```


On déchiffre "c" et on le decode de l'hexa à l'ascii :

```PYTHON
sage: flag=pow(c,d,n)
sage: flag
136143999223212922673501593262600775293
sage: hex(136143999223212922673501593262600775293).decode("hex")
'flag{l0w_n_f50f}'
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
