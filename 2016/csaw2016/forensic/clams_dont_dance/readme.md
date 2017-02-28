**Clams don't dance**

Le fichier mise à disposition pour le challenge était : out.img
```BASH
foremost out.img
```

Foremost nous extrait trois dossiers :
```BASH
mov pptx zip
```
Dans le dossier zip nous avons un fichier zip :

```BASH

unzip 00010174.zip

[Content_Types].xml  docProps  ppt  _rels
```
Le zip contient tout l'architecure d'un fichier powerpoint .

En regardant de plus près le dossier ppt/media , une image est présente dans le dossier mais absente du powerpoint

![Alt](image0.gif "image0.gif")

Pour récupérer les informations contenu dans le QRCode , on upload l'image sur le site :

[link](https://zxing.org/w/decode "Zxing.org decode")

Dans le Raw text on vois le flag apparaitre :	
```BASH
flag{TH1NK ABOUT 1T B1LL. 1F U D13D, WOULD ANY1 CARE??}
```
by ark1nar
