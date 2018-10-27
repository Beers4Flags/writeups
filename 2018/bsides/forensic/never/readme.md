# [CTF BSIDES] Write-Up - Never Too Late Mister  (Forensics)

## Description :
My friend John is an environmental activist and a humanitarian. He really hated the ideology of Thanos from the Avengers: Infinity War. He sucks at programming. He used too many variables while writing any program. One day, John gave me a memory dump and asked me to find out what he was doing while he took the dump. Can you figure it out for me?


## Analysis dump memory :


```BASH
vol.py -f Challenge.raw imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
           Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86
                      AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                      AS Layer2 : FileAddressSpace (bsides/Challenge.raw)
                       PAE type : PAE
                            DTB : 0x185000L
                           KDBG : 0x8273cb78L
           Number of Processors : 1
      Image Type (Service Pack) : 1
                 KPCR for CPU 0 : 0x80b96000L
              KUSER_SHARED_DATA : 0xffdf0000L
            Image date and time : 2018-10-23 08:30:51 UTC+0000
      Image local date and time : 2018-10-23 14:00:51 +0530
```

First, the initials of the title indicate NTLM, like other write-ups I use mimikatz plugin

```BASH
vol.py -f Challenge.raw --profile=Win7SP1x86 mimikatz
Volatility Foundation Volatility Framework 2.6
Module   User             Domain           Password 
-------- ---------------- ---------------- ----------------------------------------
wdigest  hello            hello-PC         flag{you_are_good_but 
wdigest  HELLO-PC$        WORKGROUP
```

So I find the first part of the flag.

## Tricks via volatility :

I test differents plugins such as pslist / cmdscan / consoles

```BASH
vol.py -f Challenge.raw  --profile=Win7SP1x86 consoles
Volatility Foundation Volatility Framework 2.6
**************************************************
CommandHistory: 0x300498 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 1 LastAdded: 0 LastDisplayed: 0
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x5c
Cmd #0 at 0x2f43c0: C:\Python27\python.exe C:\Users\hello\Desktop\demon.py.txt
----
Screen 0x2e6368 X:80 Y:300
Dump:
Microsoft Windows [Version 6.1.7601] 
Copyright (c) 2009 Microsoft Corporation.  All rights reserved. 
 
C:\Users\hello>C:\Python27\python.exe C:\Users\hello\Desktop\demon.py.txt
335d366f5d6031767631707f
```

Hum interesting the **demon.py.txt** file so I'm trying to get it back ...

```BASH
vol.py -f Challenge.raw  --profile=Win7SP1x86 filescan |grep "demon.py.txt"
Volatility Foundation Volatility Framework 2.6
0x000000003d4d1dc8      1      0 R--rw- \Device\HarddiskVolume2\Users\hello\Desktop\demon.py.txt
```

Nice the file seems possible to be recover

```BASH
vol.py -f Challenge.raw  --profile=Win7SP1x86 dumpfiles -Q 0x000000003d4d1dc8 -D files
Volatility Foundation Volatility Framework 2.6
DataSectionObject 0x3d4d1dc8   None \Device\HarddiskVolume2\Users\hello\Desktop\demon.py.txt
```

Shit, it's not possible !!!

However there is another possibility to recover it. 
Here is a good resource : https://www.csitech.co.uk/recreating-files-from-the-volatility-mft-parser/

It is possible to recreate the file via MFT parser

```BASH
vol.py -f Challenge.raw --profile=Win7SP1x86 mftparser | grep -C 20 "demon.py.txt"
```

I found "demon.py.txt" file with its contents, for fun I get it back

```BASH
vol.py -f Challenge.raw  --profile=Win7SP1x86 mftparser --offset=0x7ca3c00  --dump-dir=.
Volatility Foundation Volatility Framework 2.6
***************************************************************************
MFT entry found at offset 0x7ca3c00
Attribute: In Use & File
Record Number: 45487
Link count: 2


$STANDARD_INFORMATION
Creation                       Modified                       MFT Altered                    Access Date                    Type
------------------------------ ------------------------------ ------------------------------ ------------------------------ ----
2018-10-19 09:37:37 UTC+0000 2018-10-19 09:52:40 UTC+0000   2018-10-19 09:52:40 UTC+0000   2018-10-19 09:37:37 UTC+0000   Archive

$FILE_NAME
Creation                       Modified                       MFT Altered                    Access Date                    Name/Path
------------------------------ ------------------------------ ------------------------------ ------------------------------ ---------
2018-10-19 09:37:37 UTC+0000 2018-10-19 09:42:24 UTC+0000   2018-10-19 09:42:24 UTC+0000   2018-10-19 09:37:37 UTC+0000   demon.py.txt

$FILE_NAME
Creation                       Modified                       MFT Altered                    Access Date                    Name/Path
------------------------------ ------------------------------ ------------------------------ ------------------------------ ---------
2018-10-19 09:37:37 UTC+0000 2018-10-19 09:42:24 UTC+0000   2018-10-19 09:42:24 UTC+0000   2018-10-19 09:37:37 UTC+0000   DEMONP~1.TXT

$OBJECT_ID
Object ID: 4a7c2bee-7dd3-e811-aa46-080027b4bf34
Birth Volume ID: 80000000-7800-0000-0000-180000000100
Birth Object ID: 5f000000-1800-0000-6120-3d2022315f34
Birth Domain ID: 6d5f6233-7474-3372-7d22-0d0a0d0a6220

$DATA
0000000000: 61 20 3d 20 22 31 5f 34 6d 5f 62 33 74 74 33 72 a.=."1_4m_b3tt3r
0000000010: 7d 22 0d 0a 0d 0a 62 20 3d 20 22 22 0d 0a 0d 0a }"....b.=.""....
0000000020: 66 6f 72 20 69 20 69 6e 20 61 3a 0d 0a 20 20 20 for.i.in.a:.....
0000000030: 20 62 20 3d 20 62 20 2b 20 63 68 72 28 6f 72 64 .b.=.b.+.chr(ord
0000000040: 28 69 29 5e 32 29 0d 0a 0d 0a 70 72 69 6e 74 20 (i)^2)....print.
0000000050: 62 2e 65 6e 63 6f 64 65 28 22 68 65 78 22 29 b.encode("hex")
```

I can verify 

```BASH
file demon.py.txt 
demon.py.txt: ASCII text, with CRLF line terminators

cat demon.py.txt 
a = "1_4m_b3tt3r}"

b = ""

for i in a:
    b = b + chr(ord(i)^2)

print b.encode("hex")
```

## The flag :

The flag is simply the concatenation of the 2 parts

The flag is : **flag{you_are_good_but1_4m_b3tt3r}**


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
