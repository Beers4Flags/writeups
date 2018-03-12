**Network - DockerLeak - 50pts**


Enoncé :
```
During the deployment of the challenges of the THC, an attacker was able to dump the network traffic.

Can you find the flag?
```

On commence un fichier dump.pcap [Sources](sources/dump.pcap)

**Résolution :**

Comme tout challenge à 50 points l'option la plus rapide est souvent la commande strings :

```BASh
strings dump.pcap | grep -A1 -i THC{
#define FLAG "THC{d0c4ErSo(ke!m
5T_U5e_HtT6S}"

```

Flag :

```
THC{d0c4ErSo(ke!m5T_U5e_HtT6S}
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
