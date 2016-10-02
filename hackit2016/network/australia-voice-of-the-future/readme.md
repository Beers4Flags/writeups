**Australia - voice of the future (300pts network)**

EN: captured data contains encrypted information . decrypt it

Okay, it's a PCAP file with thousand frames and we look an unknown format QUIC for me.

Protocol QUIC : 
[a link][1] /  [link][2] /  [link][3] /  [link][4].

[1]: https://en.wikipedia.org/wiki/QUIC "Wikipedia"
[2]: https://github.com/google/proto-quic "Github QUIC"
[3]: https://www.chromium.org/quic/playing-with-quic "Chromium QUIC"
[4]: https://www.wireshark.org/docs/dfref/q/quic.html "Wireshark filter"

I think that protocol can be here just for pollute frames, because if I analyze PCAP file with binwalk, we see differents objects :
 - Certificate in DER format (x509 v3)
 - HTML document footer
 - gzip compressed data
 - GIF image data
 - JPEG image data, JFIF standard 1.01
 - RAR archive data,
 - ...

So inevitably we use the great tool "foremost" on PCAP and we find a "key.enc" file in rar.
```BASH
hexdump -C key.enc 
00000000  53 61 6c 74 65 64 5f 5f  d7 d5 18 2d 26 f0 07 b3  |Salted__...-&...|
00000010  44 89 4b 81 3f de 97 0d  f7 60 c9 66 06 a0 ae 73  |D.K.?....`.f...s|
00000020  9c ba f1 36 80 60 aa bc  bb bd ae d3 22 1e 4d b8  |...6.`......".M.|
```

So we know that file is salted and "D.K" may suggest "PBKDF2" but without certainty.

We decide to keep looking into PCAP file in order to find other information.
We filter 'http' in Wireshark and we find on 23962 frame that :
``̀
23902	119.862913	192.168.1.44	91.102.64.150	HTTP	475		GET /number-stations/english/e06 HTTP/1.1 
```
Description : Full request URI: http://priyom.org/number-stations/english/e06


After we go to website [link](http://priyom.org/number-stations/english/e06 "Priyom.org")
and we have a sample on page : (See e06.ogg)

In listening to the sample, we hear this channel numbers : 75948631736985999017212639734863100000


Probably the password on the "key.enc" file and as we do not know what encryption is used. Once again a big thank you to our teammate Phenol for his script on bruteforce cipher (See bf_cipher.sh)
```BASH
#!/bin/bash

CIPHERLIST="-aes-128-cbc               -aes-128-cbc-hmac-sha1     -aes-128-cbc-hmac-sha256   -aes-128-ccm               -aes-128-cfb               -aes-128-cfb1              -aes-128-cfb8              -aes-128-ctr               -aes-128-ecb               -aes-128-gcm               -aes-128-ofb               -aes-128-xts               -aes-192-cbc               -aes-192-ccm               -aes-192-cfb               -aes-192-cfb1              -aes-192-cfb8              -aes-192-ctr               -aes-192-ecb               -aes-192-gcm               -aes-192-ofb               -aes-256-cbc               -aes-256-cbc-hmac-sha1     -aes-256-cbc-hmac-sha256   -aes-256-ccm               -aes-256-cfb               -aes-256-cfb1              -aes-256-cfb8              -aes-256-ctr               -aes-256-ecb               -aes-256-gcm               -aes-256-ofb               -aes-256-xts               -aes128                    -aes192                    -aes256                    -bf                        -bf-cbc                    -bf-cfb                    -bf-ecb                    -bf-ofb                    -blowfish                  -camellia-128-cbc          -camellia-128-cfb          -camellia-128-cfb1         -camellia-128-cfb8         -camellia-128-ecb          -camellia-128-ofb          -camellia-192-cbc          -camellia-192-cfb          -camellia-192-cfb1         -camellia-192-cfb8         -camellia-192-ecb          -camellia-192-ofb          -camellia-256-cbc          -camellia-256-cfb          -camellia-256-cfb1         -camellia-256-cfb8         -camellia-256-ecb          -camellia-256-ofb          -camellia128               -camellia192               -camellia256               -cast                      -cast-cbc                  -cast5-cbc                 -cast5-cfb                 -cast5-ecb                 -cast5-ofb                 -des                       -des-cbc                   -des-cfb                   -des-cfb1                  -des-cfb8                  -des-ecb                   -des-ede                   -des-ede-cbc               -des-ede-cfb               -des-ede-ofb               -des-ede3                  -des-ede3-cbc              -des-ede3-cfb              -des-ede3-cfb1             -des-ede3-cfb8             -des-ede3-ofb              -des-ofb                   -des3                      -desx                      -desx-cbc                  -id-aes128-CCM             -id-aes128-GCM             -id-aes128-wrap            -id-aes128-wrap-pad        -id-aes192-CCM             -id-aes192-GCM             -id-aes192-wrap            -id-aes192-wrap-pad        -id-aes256-CCM             -id-aes256-GCM             -id-aes256-wrap            -id-aes256-wrap-pad        -id-smime-alg-CMS3DESwrap  -idea                      -idea-cbc                  -idea-cfb                  -idea-ecb                  -idea-ofb                  -rc2                       -rc2-40-cbc                -rc2-64-cbc                -rc2-cbc                   -rc2-cfb                   -rc2-ecb                   -rc2-ofb                   -rc4                       -rc4-40                    -rc4-hmac-md5              -rc5                       -rc5-cbc                   -rc5-cfb                   -rc5-ecb                   -rc5-ofb                   -seed                      -seed-cbc                  -seed-cfb                  -seed-ecb                  -seed-ofb "


KEY="75948631736985999017212639734863100000"
for mode in $CIPHERLIST
do
     openssl enc -d -in key.enc -out test/fil"$mode".dec -k $KEY $mode
done
```

After that operation I make a simple "strings"
```BASH
strings test/*

The good file is :
cat test/fil-aes-256-cbc.dec

```

Finally, we have the flag.

The flag is : h4ck1t{Nic3_7ry}

By team Beers4Flags
