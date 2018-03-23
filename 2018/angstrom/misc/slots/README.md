# Angstorm - CTF writeup - misc - slots - 90 pts

- Il s'agit ici d'une application de machine à sous.
- Le code source est fourni : [slots.py](src/slots.py)

- On teste une peu l'application :

```
➜  ~ nc web.angstromctf.com 3002
Welcome to Fruit Slots!
We've given you $10.00 on the house.
Once you're a high roller, we'll give you a flag.
You have $10.00.
Enter your bet: 0.2
🍐 : 🍈 : 🍈
🍉 : 🍇 : 🍒 ◀
🍒 : 🍌 : 🍒
You lost everything.
Play more to become a high roller!
You have $9.80.
Enter your bet: 0.5
🍐 : 🍌 : 🍒
🍇 : 🍌 : 🍒 ◀
🍒 : 🍇 : 🍉
You lost everything.
Play more to become a high roller!
You have $9.30.
```

- La seule donnée utilisable est la valeur de bet.
- Si on regarde en détail l'application, on se rend compte que l'on n'a aucune chances de gagner car la ligne deux est recalculée tant que l'on obtient une valeur de payout.

```python
line1 = line()
line2 = line()
line3 = line()
while payout(line2):
  line2 = line()
win = bet * payout(line2)
money += win - bet
```

- Le but étant d'obtenir le flag en bypassant les deux conditions suivantes:

```python
if money <= 0:
  req.sendall('You have no money left. Low roller.\n')
  req.close()
  return
elif money < 1000000000:
  req.sendall('Play more to become a high roller!\n')
else:
  req.sendall('Wow, you\'re a high roller!\n')
  req.sendall('A flag: {}\n'.format(flag))
  return
```


- Donc :
  - Chercher a gagner est inutile
  - Envoyer une valeur de bet négative est inutile car :
  ```python
  if bet <= 0:
    req.sendall('Sneaky, but not good enough.\n')
  ```
  - La seule solution est d'arriver à envoyer une valeur pour money qui bypass toutes les conditions.

- Une fois cette analyse effectuée la solution vient d'elle même, on envoie la valeur `nan`
- Cela va donc nous donner `nan` comme résultat de `money += win - bet`
- Mais également `nan <= 0` sera faux, tout comme `nan < 1000000000`
- On tombe donc dans notre else `Wow, you\'re a high roller!` :)

```
Welcome to Fruit Slots!
We've given you $10.00 on the house.
Once you're a high roller, we'll give you a flag.
You have $10.00.
Enter your bet: nan
🍐 : 🍈 : 🍈
🍉 : 🍇 : 🍒 ◀
🍒 : 🍌 : 🍒
You lost everything.
Wow, you're a high roller!
A flag: actf{fruity}
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
