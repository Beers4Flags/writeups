**Service Encrypt - Crypto - 200**

Enoncé :

```
I made a service to simple encrypt by giving a string.just now I forgot plaintext. Could you please decrypt it ?

Host:walked.problem.ctf.nw.fit.ac.jp
port:4000

Contenu de info.txt

556d633950513d3d5632463a51523e3e586d473b52533f3f5d5b663c535440405e4a493d545541415e364a3e555642425d4e693f565743435b724c40575844445f744d415859454560516c42595a464661776d435a5b4747627650445b5c4848653f6f455c5d4949675570465d5e4a4a656453475e5f4b4b687a54485f604c4c6758734960614d4d6569744a61624e4e6669754b62634f4f6c43584c636450506e80594d64655151
```

__Résolution :__

Le service mis à disposition nous renvoie un block de 16 byte lors qu'on lui envoie un caractère :

```
nc walked.problem.ctf.nw.fit.ac.jp 4000
F
556d633950513d3d
FF
556d633950513d3d566e643a51523e3e
FI 
556d633950513d3d5632463a51523e3e
```

Le même caractère répétés ne renvoi pas le même bloc de chiffré.

On découpe notre chiffré en 21 blocs de 16 byte.

On va tester le retour de chaque lettres au fur et à mesure de l'avancé de notre flag :

```
Pour :
F => on va chercher le retour 556d633950513d3d => soit bloc[0]
Pour :
FI => 556d633950513d3d5632463a51523e3e => bloc[0]+bloc[1]
Pour :
FIT => 556d633950513d3d5632463a51523e3e586d473b52533f3f => soit bloc[0]+bloc[1]+bloc[2]
```

Et ainsi de suite jusqu'à trouvé le flag complet :

```PYTHON
import socket
import string

flag="FIT{uq_4e_fdswal_32p"

bloc=["556d633950513d3d","5632463a51523e3e","586d473b52533f3f","5d5b663c53544040","5e4a493d54554141","5e364a3e55564242","5d4e693f56574343","5b724c4057584444","5f744d4158594545","60516c42595a4646","61776d435a5b4747","627650445b5c4848","653f6f455c5d4949","675570465d5e4a4a","656453475e5f4b4b","687a54485f604c4c","6758734960614d4d","6569744a61624e4e","6669754b62634f4f","6c43584c63645050","6e80594d64655151"]
alphabet=string.printable

hote = "walked.problem.ctf.nw.fit.ac.jp"
port = 4000
 

superbloc=bloc[0]+bloc[1]+bloc[2]+bloc[3]+bloc[4]+bloc[5]+bloc[6]+bloc[7]+bloc[8]+bloc[9]+bloc[10]+bloc[11]+bloc[12]+bloc[13]+bloc[14]+bloc[15]+bloc[16]+bloc[17]+bloc[18]+bloc[19]+bloc[20]


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hote,port))
 
for carac in alphabet:
  Request = flag+carac+"\r"
  s.send(Request)
  data = s.recv(1024)
  if superbloc in data:
    print "le caractere est : "+str(carac)
    print data
    break 

#flag : FIT{uq_4e_fdswal_32p}
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
