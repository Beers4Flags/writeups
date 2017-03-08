**OTPCards - 50pts**


![Alt](img/card1.png "Punched Card 1")

![Alt](img/card2.png "Punched Card 2")


Nous avions à disposition deux cartes perforés de chez IBM.


Pour récupérer les données contenu de dans , nous les avons uploader sur ce site :

http://www.masswerk.at/cardreader/

On obtient deux chaines en hexa :


Carte 1 = 365C997610306888C3CB07B26C7ED39325E4AD1BDC87255B8F5E54B66E253759B306A9BAA01B7D4A

Carte 2 = 5A04DC351E3D7B9CC3CE1DFF5142B08B3AFCA60B9484336B961F54A67319304E8845ABA9B60C734A

L'OTP du titre nous fait penser à un masque jetable. Celui-ci aurait été utilisé pour chiffré les deux plaintext.

https://github.com/SpiderLabs/cribdrag

Nous utilisons le script xorstrings.py de l'outil cribdrag pour xorer les deux chaines.

```BASH
./xorstrings.py 365C997610306888C3CB07B26C7ED39325E4AD1BDC87255B8F5E54B66E253759B306A9BAA01B7D4A 5A04DC351E3D7B9CC3CE1DFF5142B08B3AFCA60B9484336B961F54A67319304E8845ABA9B60C734A

=> 6c5845430e0d131400051a4d3d3c63181f180b1048031630194100101d3c07173b43021316170e00
```

Nous utilisons ensuite la technique du crib sur cette chaine.

```BASH

./cribdrag.py 6c5845430e0d131400051a4d3d3c63181f180b1048031630194100101d3c07173b43021316170e00


Your message is currently:
0 ________________________________________
Your key is currently:
0 ________________________________________
Please enter your crib: punched cards
0: "-+ fhw4cdh)N"
1: "(0-mevp f{?YO"
2: "56`n{qd%y,OX"
3: "3{cp|ea:.\Nk"
...
26: "pes_or_cards}"
27: "`hRd^'"pwejs"
Enter the correct position, 'none' for no match, or 'end' to quit: 26

Is this crib part of the message or key? Please enter 'message' or 'key': message
Your message is currently:
0 __________________________punched cards_
Your key is currently:
0 __________________________pes_or_cards}_

```

On continu ainsi en testant des mots potentiel jusqu'à obtenir le flag.

thcon{punched_tapes_or_cards}


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
