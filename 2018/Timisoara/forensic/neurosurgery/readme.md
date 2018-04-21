# [CTF TIMISOARA] Write-Up - Neurosurgery  (Forensics, 250)

## Description :
I consider biology classes the most fun of all and sometimes scary.
For example, in the last lesson we learned about brain dumping. It
was extraordinary (black magic as my dad said, btw he's a computer
scientist), learning about interactions and activities in the memory.

What? Yes, of course you can look at it, too. The pleasure is mine!


## Image analyse :

Premièrement, il faut déterminer ce que représente ce fichier.

```BASH
file image 
image: ELF 64-bit LSB core file x86-64, version 1 (SYSV)
```

Au vu de la taille du fichier, je pense immédiatement à un dump mémoire.

Pour le confirmer, quelques petits strings opportuns :

```BASH
strings image | grep -iEo '(linux|ubuntu|debian|windows)' | sort | uniq -c | sort -n
      5 DEBIAN
      6 UBUNTU
     10 WindowS
     14 WINDOWS
     66 windows
     96 debian
     98 LINUX
    105 Windows
    524 Debian
    631 Linux
   3396 Ubuntu
   3682 ubuntu
  10270 linux


strings image | grep BOOT_
BOOT_IMAGE=/boot/vmlinuz-4.4.0-116-generic root=UUID=1754a0a8-08f8-4877-9489-b4e70e52d59a ro
BOOT_IMAGE=/boot/vmlinuz-4.4.0-116-generic
Command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-116-generic root=UUID=1754a0a8-08f8-4877-9489-b4e70e52d59a ro
Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-116-generic root=UUID=1754a0a8-08f8-4877-9489-b4e70e52d59a ro
BOOT_IMAGE=/boot/vmlinuz-4.4.0-116-generic
^C


strings image |grep amd64
Linux version 4.4.0-116-generic (buildd@lgw01-amd64-021) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.9) ) #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 (Ubuntu 4.4.0-116.140-generic 4.4.98)

https://packages.ubuntu.com/linux-image-4.4.0-116-generic

strings image |grep xenial
DISTRIB_CODENAME=xenial
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```

Nous pouvons conclure qu'il s'agit d'un dump mémoire d'une distribution Linux de type Ubuntu avec un kernel en 4.4.0-116-generic. Au vu du kernel, il s'agirait de la version Xenial chez Ubuntu.



## Création du profil :

Il faut donc installer dans une VM le bon kernel dans une distribution Ubuntu Xenial x64 afin de créer le profil adéquat :

```
sudo apt install libelf-dev git zip make volatility linux-image-4.4.0-116-generic linux-headers-4.4.0-116-generic
git clone https://github.com/tomhughes/libdwarf.git libdwarf
cd libdwarf/libdwarf
./configure
sudo make
cd ..
cd dwarfdump
./configure
make
sudo make install
cd volatility/tools/linux/
sudo make  -C /lib/modules/4.4.0-116/build CONFIG_DEBUG_INFO=y M= modules
dwarfdump -di ./module.o > module.dwarf
sudo zip Ubuntu1604_4.4.0-116.zip module.dwarf /boot/System.map-4.4.0-116-generic
```

Je vérifie ensuite que volatility le détecte.

```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux --info |grep "Profile" | grep "Ubuntu"
LinuxUbuntu16041x64          - A Profile for Linux Ubuntu16041 x64
LinuxUbuntu1604_4_4_0-116x64 - A Profile for Linux Ubuntu1604_4.4.0-116 x64
LinuxUbuntu1604x64           - A Profile for Linux Ubuntu1604 x64
```

## Analyse via volatility :

Maintenant que le profil est détecté, je vérifie qu'il marche bien :-)
```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux -f image --profile=LinuxUbuntu1604_4_4_0-116x64 linux_bash
Volatility Foundation Volatility Framework 2.6
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1166 bash                 2018-04-15 15:24:47 UTC+0000   cd ..
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls
    1166 bash                 2018-04-15 15:24:47 UTC+0000   sudo rm /media/sf_bin/
    1166 bash                 2018-04-15 15:24:47 UTC+0000   cd .cache/
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls
    1166 bash                 2018-04-15 15:24:47 UTC+0000   sudo su
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:24:47 UTC+0000   poweroff
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:24:47 UTC+0000   sudo chown panda:panda ht0p 
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls
    1166 bash                 2018-04-15 15:24:47 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:24:47 UTC+0000   sudo umount /media/sf_bin 
    1166 bash                 2018-04-15 15:24:47 UTC+0000   sudo rm -r /media/sf_bin/
    1166 bash                 2018-04-15 15:24:47 UTC+0000   chown panda:panda ht0p 
    1166 bash                 2018-04-15 15:24:47 UTC+0000   chown panda:panda suleanu
    1166 bash                 2018-04-15 15:24:47 UTC+0000   mv suleanu ht0p
    1166 bash                 2018-04-15 15:24:49 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:24:55 UTC+0000   shred -u .bash_history 
    1166 bash                 2018-04-15 15:24:59 UTC+0000   ls
    1166 bash                 2018-04-15 15:25:02 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:25:21 UTC+0000   ls /media/
    1166 bash                 2018-04-15 15:25:24 UTC+0000   ls -la
    1166 bash                 2018-04-15 15:25:30 UTC+0000   ./ht0p \  &
    1166 bash                 2018-04-15 15:25:32 UTC+0000   htop
    1166 bash                 2018-04-15 15:25:32 UTC+0000   htop
```


Nous voyons qu'un binaire nommé "ht0p" est copié sur la machine puis et lancé juste avant le binaire légitime "htop"

Je regarde maintenant les processus qui sont éxécutés sur la machine :
```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux -f image --profile=LinuxUbuntu1604_4_4_0-116x64 linux_pslist
....
0xffff88007a075400 bash                 1166            1084            1000            1000   0x0000000035720000 2018-04-15 15:25:24 UTC+0000
0xffff8800355e3800 ht0p                 1192            1166            1000            1000   0x000000007b982000 2018-04-15 15:26:06 UTC+0000
0xffff8800355e6200 htop                 1193            1166            1000            1000   0x000000007b9a2000 2018-04-15 15:26:08 UTC+0000
```

Souhaitant en savoir plus sur le process "ht0p", je lance alors la commande linux_proc_maps sur le PID du process :
```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux -f image --profile=LinuxUbuntu1604_4_4_0-116x64 linux_proc_maps -p 1192
Volatility Foundation Volatility Framework 2.6
Offset             Pid      Name                 Start              End                Flags               Pgoff Major  Minor  Inode      File Path
------------------ -------- -------------------- ------------------ ------------------ ------ ------------------ ------ ------ ---------- ---------
0xffff8800355e3800     1192 ht0p                 0x0000000000400000 0x00000000004d9000 r-x                   0x0      8      1     390593 /home/panda/ht0p
0xffff8800355e3800     1192 ht0p                 0x00000000006d8000 0x00000000006dd000 rw-               0xd8000      8      1     390593 /home/panda/ht0p
0xffff8800355e3800     1192 ht0p                 0x00000000006dd000 0x00000000006e4000 rw-                   0x0      0      0          0 
0xffff8800355e3800     1192 ht0p                 0x0000000001f77000 0x0000000001f9a000 rw-                   0x0      0      0          0 [heap]
0xffff8800355e3800     1192 ht0p                 0x00007ffd8ff80000 0x00007ffd8ffa1000 rw-                   0x0      0      0          0 [stack]
0xffff8800355e3800     1192 ht0p                 0x00007ffd8ffeb000 0x00007ffd8ffee000 r--                   0x0      0      0          0 
0xffff8800355e3800     1192 ht0p                 0x00007ffd8ffee000 0x00007ffd8fff0000 r-x                   0x0      0      0          0 [vdso]
```


Je vois que le binaire est stocké dans le $HOME de l'utilisateur panda, j'essaye donc de voir si le fichier est récupérable via son inode :
```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux -f image --profile=LinuxUbuntu1604_4_4_0-116x64 linux_find_file -F "/home/panda/ht0p"
Volatility Foundation Volatility Framework 2.6
Inode Number                  Inode File Path
---------------- ------------------ ---------
          390593 0xffff88007bd8e698 /home/panda/ht0p
```

Il se trouve que oui, nous obtenons donc bien un inode sur le fichier.

Il ne reste plus qu'à le télécharger.
```BASH
volatility --plugins=/usr/share/volatility/contrib/plugins/overlays/linux -f image --profile=LinuxUbuntu1604_4_4_0-116x64 linux_find_file -i 0xffff88007bd8e698 -O ht0p
...
file ht0p 
ht0p: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID[sha1]=015d3ac9f4ba50287e556b432120e468916710ce, stripped

```


## The flag :

Maintenant que nous avons le binaire et avant de partir avec IDA sur ce dernier, rendons-le éxécutable pour voir ce qu'il affiche :

```BASH
./ht0p 
****\/\/-- timctf{ch4nc3_f4vors_th3_pr3p4red_m1nd} --\/\/**** 
```

Finalement, il n'y a pas besoin de reverse le binaire ;-)

Le flag est : **timctf{ch4nc3_f4vors_th3_pr3p4red_m1nd}**


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
