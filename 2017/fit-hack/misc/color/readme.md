**Color - 250pts**

Check the color information.


So we have a PNG file !

![Alt](img/image.png "initial PNG")


When you have a PNG file often your reflex is to analyze precisely headers / embedded files /..

```BASH
hd -n 256 image.png 
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 01 2c 00 00 01 2c  08 03 00 00 00 4e a3 7e  |...,...,.....N.~|
00000020  47 00 00 00 08 61 63 54  4c 00 00 00 12 00 00 00  |G....acTL.......|
00000030  00 93 6d 04 f2 00 00 00  39 50 4c 54 45 12 12 12  |..m.....9PLTE...|
00000040  46 49 54 47 72 61 5f 4e  33 5f 50 30 62 6c 33 63  |FITGra_N3_P0bl3c|
00000050  35 5f 64 33 72 66 75 6c  69 35 5f 69 6d 61 70 68  |5_d3rfuli5_imaph|
00000060  69 72 6b 5f 72 74 61 74  33 64 74 77 30 77 30 6e  |irk_rtat3dtw0w0n|
00000070  7b 41 6e 7d 00 00 47 1d  c5 19 00 00 00 01 74 52  |{An}..G.......tR|
00000080  4e 53 00 40 e6 d8 66 00  00 00 1a 66 63 54 4c 00  |NS.@..f....fcTL.|


strings image.png 
...
FITGra_N3_P0bl3c5_d3rfuli5_imaphirk_rtat3dtw0w0n{An}

```


Hum hum It looks great as a flag pattern FIT{...}, but letters seem to be mixed


We know too software which used ofr this image :
```BASH
exiftool image.png 
...
Software                        : APNG Assembler 2.9
```

Oki so I used a tool specially for APNG format : apngdis
```BASH
pngdis image.png 

APNG Disassembler 2.5

Reading 'image.png'...
extracting frame 1 of 18
extracting frame 2 of 18
extracting frame 3 of 18
extracting frame 4 of 18
extracting frame 5 of 18
extracting frame 6 of 18
extracting frame 7 of 18
extracting frame 8 of 18
extracting frame 9 of 18
extracting frame 10 of 18
extracting frame 11 of 18
extracting frame 12 of 18
extracting frame 13 of 18
extracting frame 14 of 18
extracting frame 15 of 18
extracting frame 16 of 18
extracting frame 17 of 18
extracting frame 18 of 18
all done
```

Well we have now 18 images but apart from the color that changes nothing else !!

Suddenly I remember the description of the challenge : "Check the color information"

```BASH
R = 70
G = 73
B = 84

So in decimal (70 73 84) -> hex (46 49 54) -> ascii = FIT
```

This is the only possible track to get the flag, in order to do this I use the product : stegpy
https://github.com/Baldanos/Stegpy


And with one liner in BASH ;-) you have the flag
```BASH
for i in {01..18}; do printf $(printf '\%o' $(python stegpy.py apng/apngframe$i.png -C -p color_info | grep -v "Alpha" | grep "distribution" | cut -d':' -f 2 | sed -e 's/\[\([0-9]*\).*/\1/;s/ //g' | tr '\n' ' ')) ;done
FIT{Animat3d_P0rtabl3_N3tw0rk_Graphic5_i5_w0nd3rful}
```


The flag is : FIT{Animat3d_P0rtabl3_N3tw0rk_Graphic5_i5_w0nd3rful}

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
