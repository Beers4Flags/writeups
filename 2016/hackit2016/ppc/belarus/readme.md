# Belarus

For this challenge, we received a very big pain.txt file ! Pure madness.
50MB of data, so our first step was trying to open it in any editor, just to know what it looked like.

Hopefully, makhno was using the geany, who was able to open it correctly.

After some time, I realized we could open it too with vim using the :set nowrap command.

Vim uses better memory usage, so I read the first some chars... :

```
ffd8ffe000104a46494600010100004800480000ffe1004c4578696600004d4d002a000000080002011200030000000100010000876900040000000100000026000000000002a00200040000000100000514a003000400000001000000db00000000ffe10921687474703a2f2f6e732e61646f62652e636f6d2f7861
```

Our famous bot-helper told me that was a JFIF file encoded here, but it was hardly readable that easily.

First step :
Changing e29684 (representing the viewable things in the file) by 1, so we can easily parse the file.
Script (read_pain.py)

Second step :
Find how many space 1 letter takes : 13 length, using vim and a fastly programmed py script.
Last step, find a way to transform these letter into the correct hex value:
Script (read_out.py)

Now we had a bunch of values like 2000 or more, compare it to our previously retrieved data:
Big values:

```
2161,2161,3353,4319,2161,2161,3659,3999,3999,3999,2773,3999,2995,3472,2995,4155,2995,4339,2995,4155,3999,3999,3999,2773,3999,2773,3999,3999,3999,3999,2995,4319,3999,[...]
```

Replace it was known values: (2161 == f, ...)

```
ffd8ffe000104a46494600010100004800480000ffe1004c4578696600004d4d002a000000080002011200030000000100010000876900040000000100000026000000000002a00200040000000100000514a003000400000001000000db00000000ffe10921687474703a2f2f6e732e61646f62652e636f6d2f7861
```
Some search and replace to have the correct values for the full file.

Then I used the read_hex.py script to morph the hex data into a flag.jpg

We could read the flag on that image !


By Birdy42
