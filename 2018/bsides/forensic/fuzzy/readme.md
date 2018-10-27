# [CTF BSIDES] Write-Up - FuzzY (Forensics)

## Description :
Bob and Charlie were sending some messages among themselves,and I planned to intercept their messages and get something out of it, however, they are clever enough that no secret gets leaked. Please help me out to get the secret!!


## Analysis PCAP :

As for any pcap, I use *strings* command

```BASH
strings final_fuzz.pcap
...
-----BEGIN PGP MESSAGE-----
Version: OpenPGP v2.0.8
Comment: https://sela.io/pgp/
wcBMA8fXP+32fyviAQf/T+NzsOgQ+ejW16GeK6h9WS9IDelAN9GLY5x5o9ilBlEL
G4IPati4/zqd+kyV5mmA7k2eKnNByRnxElpp0PoGULX0ykjBTcXuLtNXzGWcDsFF
xAkH8PduoPCcnNGWrCU6D8ZuWNtp7oeZ1krUZP+Kg9sfjjKfx0aUFhWs9SQH6mif
AlbJQwxKi2xXv0UsHvg4Mz4TpVstoO5XcN9d4V+gygc+wx0K61JwAFw96xptNi9y
hdMz/c7yW56JwBfwyiHvYmgLdWYJW9OEoQIj7Rwh1v8mD846vbvEDmagQ0Ra/K6q
lnxa37gBFE+4kYpSXP7yqr8QMhmGDpMROJoJqxYyY9JxAe6317HZ+UUEOmNR+0tB
EmPl/VVaoPc5q6RQ/cxwY4VhR4DtPsG9Gw237Sx+xSTAG5JbmtBf4KfQdVbeaXn1
PYPYBeCVL6nb6uPz6ZHBJ2SODWg9+Ssas+Gd5P7Q0zSA/35qYdamnAqUM/ujM2nN
k2U=
=+x+V
-----END PGP MESSAGE-----
...
```

Hum, I found a PGP message with a URL in order to decipher so I must find :
1. a passphrase
2. a private key PGP


Then I often test the *binwalk* command on PCAP file

```BASH
binwalk final_fuzz.pcap 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1131          0x46B           PNG image, 200 x 200, 8-bit/color RGBA, non-interlaced
1172          0x494           Zlib compressed data, default compression
8588          0x218C          PGP armored data, message
109369        0x1AB39         Zlib compressed data, default compression

```

Oh there is a PNG image however *binwalk* or *foremost* are not able to recover it.

## Wireshark :

I can do a *string* in Wireshark

The image is interesting for : ![Alt](files/fuzzy_dns_filter01.png) 

1. I can parse hexadecimal for PNG header (89 50 4e 47)
2. I can see result in hexadecimal  
3. I can see PNG / IHDR / IDAT 

So I can filter only such as 
![Alt](files/fuzzy_dns_filter02.png)

1. The filter in Wireshark *dns && ip.src==192.168.42.129*
2. The hidden data is always begin in *00e0* position
3. The hidden data is always finish in *01e0*

Endly we can see the end header from PNG image :
![Alt](files/fuzzy_dns_filter03.png)


I can recover all values in hex such as [hex_png.log](files/hex_png.log)

```BASH
cat hex_png.log | awk '{print $2 $3 $4 $5 $6 $7 $8 $9 $10 $11 $12 $13 $14 $15 $16 $17}' | tr -d '\n' | sed -e 's/x//g' | xxd -r -p > img.png
file img.png 
img.png: PNG image data, 200 x 200, 8-bit/color RGBA, non-interlaced
```

Nice the file is now a beautiful qrcode
![Alt](files/img.png)

```BASH
zbarimg img.png 
QR-Code:-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: BCPG C# v1.6.1.0

lQOsBFvO/9wBCACgT4fK4dJm+M14jotXPUeKueo8xfFDunNUx/ZaSQbp5Y0i64OZ
dPkQk4E2zCgXaYKNRhiIx2RUy27GBf7xjtDb0gh/HNhC41f5ZzYrNQBEcabcr0hn
VfwiEzAqmTg+5TNsG26ZD2kuO1/J5zbKxI1D3g/9//fe5Nw8GucDiOntKgvFEXeV
ETZ0llbP/mh8SAn5+naJiJJri9y3GF+QhX7wYP+W6mBkano8X/Yk2B2qWIRT6wRU
DMQy1ptavyv5EJhYbsQGeAMu7WPJN+mLutAE2E1Xj03Sevsx2ynN8b/jF/HYp/mZ
SzZ+TbHlRUoMC4+hYh5XfXy7Cx9HSI0uIDShABEBAAH/AwMCEv0ZoXbeXxxg3ioH
/Y0lUhYOormsNzbrBjl1ipyWTDmRAf9BhmAPrX9K5GPAFAurGOj8QOQEWGrOyXfk
gYtHXzGk1K6ItCitgxdBqHgbti23Ht8SmVWw3/pijPXXerXXMqj6NQ95ma6bYPsU
PRtE1qtiEs+T8ln6ZBU9BCNyuZDceBY6btZS0cp88wB1xEPorhXVtjiV1cjDRSFG
licqXh4fr4Qe0TUEeZK1uTqlhdj6YvKoFP94OKGxeM0eR1R/H/zyOtJVMMsEZLGr
GNSVBZBN0B6l9wAMa+DGpuHIX25I197vP3x0v0gvP/57bF9og9mj2JzntM9NJsR1
2zAgplgX4IUp4SGPvcNbLE5c9yIEj77SAOBumrF3IcUYNN9IXvIHQh8qzOWmI5q+
NFCKin0tQNCAx4ef+4ThkyPezRovlFxG6T4HMF1YjYrlVMgiN034opaCKoFXd3EF
4UufN3vV0IYB7AfxWLeNAJyPCreDSyYyLFGx+ONpM5JKk/1cwH8H0XQuLXY+TuGj
iF6QWkRkVcAYv0F7r2wPaVOVa8465s34fY94Rv1+KCpsjNFc3FrAJhz84jETxxqr
s44U/zmGh0/tixjs9vB1C/i7csYWXYJYiPsPmcp5sOE4M1PtYsIfuOlaJ12e/IV9
YnNK+RLghYQ0MghUMHZeg8aqKY7SATDB1SuK+YKmhXte/E/VhTBUy+3RautMIUwS
w9R1z2Hh4POZ4kp8yj9PnEujoQ5XtZuruhNyiWEwWYf1GPuDSoeEYcIRj18h8dL+
OSvsS1DqgPxH9hy8iidLDq1ZkrQ0w08Du9zjVY02f4OoRunzXbis6P3Y0mRf4iif
bYdqVg3snMwY5u9lEaIYqmtcGibgybah394CgTt0xrQTa2FydGlrOTk3QGdtYWls
LmNvbYkBHAQQAQIABgUCW87/3AAKCRDH1z/t9n8r4qnlB/9N1BBWSf6lfmejPh3R
DZ+QrBsCELm8qBeawlsY9To6UUdrIoC9vzIwKAgil2K2MC9z/laZQcep0WepnOar
5KSUyhPI50/aE97yfA0v4lKkylb0OPt8E0S4gIxTlRhpht2K4lsRaD+2wyRvMRuU
/Grgxd5TVVm9KfXQBCAxgFgX2OdZ2/Yb2GJQ4M6DquISIBar+i39a9bdZ9kP70ox
jfgG8SLXPxzBiHIULUy4X+80VafKWw1/AzN2t4CTRtIMHu7jeUqpws+MB6TxTLBA
G/JSdb+W3ceHseJ9YXqVIhfrlKt8T3QAqErjQjPN0YB9KDaELwDM1rxFryy8zuAB
zdZ/
=rb5z
-----END PGP PRIVATE KEY BLOCK-----
```

Ok ok I found just the private key but where is the passphrase ?

```BASH
exiftool img.png | grep Description
Image Description               : helloworld
```

I recap I have in my possession :
1. a message PGP
2. a private key PGP
3. a passphrase


## The flag :

You can go on : https://sela.io/pgp/

The flag is : **flag{eNcryP7!ng_t0_PgP_1s_r34LLy_Pre3tY_g00D_pr1V4cY}**


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
