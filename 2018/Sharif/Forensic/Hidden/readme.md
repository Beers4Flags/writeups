**Web - Hidden  - 100pts**

Enoncé :
```
Find the hidden process
```

**Résolution :**

On cherche un pid caché, on analyse tout d'abord le dump avec Volatility :

```BASH
volatility -f dump imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/ark1nar/ctf/sharif/forensic/dump)
                      PAE type : PAE
                           DTB : 0x359000L
                          KDBG : 0x80545c60L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2018-01-28 17:35:20 UTC+0000
     Image local date and time : 2018-01-28 21:05:20 +0330
```

Le profile est : **WinXPSP2x86**

On dump les process avec deskscan

```BASH
volatility -f dump --profile=WinXPSP2x86 deskscan
Volatility Foundation Volatility Framework 2.6
**************************************************


Desktop: 0x3897678, Name: SAWinSta\SADesktop, Next: 0x0
SessionId: 0, DesktopInfo: 0xbcbe0650, fsHooks: 0
spwnd: 0xbcbe06e8, Windows: 3
Heap: 0xbcbe0000, Size: 0x80000, Base: 0xbcbe0000, Limit: 0xbcc60000
**************************************************
Desktop: 0x1156760, Name: WinSta0\Default, Next: 0x810b54a0
SessionId: 0, DesktopInfo: 0xbc630650, fsHooks: 0
spwnd: 0xbc6306e8, Windows: 95
Heap: 0xbc630000, Size: 0x300000, Base: 0xbc630000, Limit: 0xbc930000
 1612 (csrss.exe 620 parent 548)
 1464 (explorer.exe 1576 parent 1444)
 432 (explorer.exe 1576 parent 1444)
 1360 (vmtoolsd.exe 404 parent 1576)
 1872 (explorer.exe 1576 parent 1444)
 1104 (explorer.exe 1576 parent 1444)
 912 (wscntfy.exe 920 parent 1024)
 408 (vmtoolsd.exe 404 parent 1576)
```
Le pid caché est le **404** du processus vmtoolsd.exe, le format du flag est le suivant :
```
The flag is SharifCTF{MD5(Process id)}.
```
Le flag qui valide  : 
```
SharifCTF{4f4adcbf8c6f66dcfc8a3282ac2bf10a}
```


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
