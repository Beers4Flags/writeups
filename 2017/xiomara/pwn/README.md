* mint est un pwn reposant sur un buffer overflow. Celui ci s'obtient en créant un texte puis en luis rajoutant un deuxième texte. Il est alors possible d'écraser le retour de main_proc. Le principe ici est de faire un premier ROP affichant la valeur GOT de puts, puis de reboucler en 0x080483dd. À cet instant, connaissant l'adresse libc de puts, on est en mesure de faire un system(/bin/sh).

* xor_tool semble présenter deux failles dans la fonction decrypt, un BOF de 4 octets via  read(0, s, 0x36u) où s est un buffer de 50 octets, et une faille format via un printf direct du texte déchiffré.
payloadformat.py exploite cette deuxième faille de la façon suivante:
 	- affichage de la pile
	- affichage de la valeur GOT de printf
	- Ecrasement du retour de decrypt vers system(/bin/sh), l'écriture de la pile se fait en bouclant sur la fonction decrypt en modifiant à chaque fois l'adresse de retour (0x8048907) en 0x8048902.


François
