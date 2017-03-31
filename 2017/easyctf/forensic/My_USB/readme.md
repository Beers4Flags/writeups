**Forensic - My USB - 150pts**

Un dump d'une clé USB est fournit dans l'énoncé du challenge.

```BASH
Description:

Written by neptunia

I found my usb from a long time ago. I know there's a flag on there somewhere; can you help me find it?
Hint:  Sorry, no hint. 

File = usb.img

```

Résolution :

```BASH
formemost usb.img

Foremost version 1.5.7 
Invocation: foremost 2c370b79d147127064f019dcb05bba1aa917c552_usb.img 
 
Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00002201.jpg 	      87 KB 	    1127233 	 
1:	00002375.jpg 	      50 KB 	    1216472 	 
2:	00002494.jpg 	      53 KB 	    1276928 	 
3:	00000696.zip 	     748 KB 	     356352 	 
4:	00002194.docx 	     149 KB 	    1123328 	 
5:	00000064.png 	     315 KB 	      32768 	  (1680 x 1316)
Finish: Tue Mar 14 13:52:07 2017

6 FILES EXTRACTED
	
jpg:= 3
zip:= 2
png:= 1
------------------------------------------------------------------
```

Dans l'image 00002494.jpg le flag :

![Alt](img/00002494.jpg "Flag")


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
