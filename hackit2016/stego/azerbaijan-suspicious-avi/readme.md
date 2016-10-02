**Suspicious AVI (stego 450pts)**

EN: The information security expert has begun to create lessons for cyberarmy, but he is a spy on a twist of fate ! Your task is to check one of his video lessons regarding transfer of the secret information. 

First, we have a video : avi.avi . It's a video on Pepa pig ;-)

So the first instinct is to find information on video :

You can use exiftool / ffmpeg :
```BASH
ffmpeg -i avi.avi
...
Input #0, avi, from 'avi.avi':
  Metadata:
    copyright       : http://countersite.org/images/hehehe.avi
```

Interesting information with a link to another video : http://countersite.org/images/hehehe.avi

Hum hum it looks like the same video !!!

After another time exiftool and/or ffmpeg : no interesting information is found

Now we must find the differences between two videos.

Two possibilities are to compare on :
 - video
 - sound

First, we extract sound from each video
```BASH
ffmpeg -i avi.avi avi.wav
ffmpeg -i hehehe.avi hehehe.wav
```

But on sound no difference to found

So it remains on the comparison videos

With foremost we can extract images from each video in order to compare the possible difference
```BASH
foremost avi.avi
foremost hehehe.avi
```
We have two directories with exactly the same number of picture, so we want compare each image from two directories. We use 'compare' from imagemagick in a script.
```BASH
#!/bin/bash
for i in *.png; do
	compare output_avi/$i output_hehehe/png/$i compared/compared_$i
done
```

The result is a comparison of the two other, we look the new images and ... a good surprise on image : compared_00057406.png

We can see a red line at the top of the image. Hum hum probably the stegano with LSB :-)

![Alt](compared_00057406.png "compared_00057406.png")

Then a big thank you to our teammate Phenol for his script on LSB (See h4ck1t_pepapig.py)

```Python
#!/usr/bin/env python

import sys
import cv2

#./h4ck1t_pepapig.py vidz.png rgb 8 1 464

def recompose(lsb_str, byte_len):
    byte_lst = []
    nwstr = "".join([ chr(int(lsb_str[i:i+byte_len],2)) for i in range(0,len(lsb_str),byte_len) ])
    return str(nwstr)


def compare(maxpx, ch):
    im0 = cv2.imread("vidz.png")
    im1 = cv2.imread("vidz-orig.png")
    line, col, band = im0.shape
    bit_str = ""
    for x in range(0, line):
        for y in range(0,col):
            for z in ch:
                if x*y < maxpx:
                    print "Original ("+str(x)+" "+str(y)+" "+str(z)+") => "+str(im1[x,y,z])
                    print "Modified ("+str(x)+" "+str(y)+" "+str(z)+") => "+str(im0[x,y,z])
                    bit_str += str( im1[x,y,z] - im0[x,y,z])
                else:
                    return bit_str

nbcol = int(sys.argv[4])
chan = { 'r' : 2, 'g' : 1, 'b' : 0, 'a' : 3 }
ch = [ chan[sys.argv[2][i]] for i in range(0,len(sys.argv[2]))]
maxpx = int(sys.argv[5])
bytelen = int(sys.argv[3])

bit_str = compare(maxpx, ch)
print bit_str
print recompose(bit_str,bytelen)

lsb_str = ""
img = cv2.imread(sys.argv[1])
line, cols, bands = img.shape
for x in range(0, line):
    for y in range(0,cols, nbcol):
        for z in ch:
            if x*y > maxpx:
                break
            lsb_str += str(img[x,y,z] & 1)
print lsb_str
found = recompose(lsb_str,bytelen)
print found
```

Through its scripts, we can see brainfuck on image compared
```Bash
.+[----->+++<]>+.[-->+<]>.--[->++<]>-.++++++++.-[-->+<]>----.[--->++<]>--.+++++++.-[->+++++<]>.[--->+<]>----.[-->+<]>-----.---.-[----->+<]>--.---------------.++++++++++++++.+++.[-->+<]>----.----[->++<]>-.+++++++++.[-->+<]>.--[->++<]>-.++++++++.-[-->+<]>--.-[->++<]>.>--[-->+++<]>.......
```

In the end we send brainfuck on online decoder and it's finish we have the flag.

The flag is : h4ck1t{br41n_mp4_h4ck3d}

by team Beers4Flags
