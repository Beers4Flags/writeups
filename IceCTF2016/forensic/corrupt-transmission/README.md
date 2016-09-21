# corrupt transmission (forensic · 50 pt)

We intercepted this image, but it must have gotten corrupted during the transmission. Can you try and fix it?

the .PNG file seems to be corrupt

With PNGCHECK : 

```
root@kali:~/Bureau# pngcheck -v corrupt_92cee405924ad39fb513e3ef910699b79bb6d45cc5046c051eb9aab3546e22c3.png 
File: corrupt_92cee405924ad39fb513e3ef910699b79bb6d45cc5046c051eb9aab3546e22c3.png (469363 bytes)
  File is CORRUPTED.  It seems to have suffered EOL conversion.
  It was probably transmitted in text mode.
```


The header of the PNG file has been modified in his first 8 octets has we can see with :  
```
root@kali:~/Bureau# xxd -l8 corrupt_92cee405924ad39fb513e3ef910699b79bb6d45cc5046c051eb9aab3546e22c3.png 
0000000: 9050 4e47 0e1a 0a1b  
```


A png normal header is : 89 50 4E 47 0D 0A 1A 0A.

If we correct the header, the picture show us the flag :)


eilco



