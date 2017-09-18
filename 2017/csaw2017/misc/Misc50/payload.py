#!/usr/bin/python
from pwn import *

p=remote('misc.chal.csaw.io', 4239)

p.recvuntil("mit.\n")
gdeb=p.recvuntil("\n")
s=""

def lit(s):
    p.sendline(str(s))
    b=p.recvuntil("\n")
    return(b)

def init():
    m=[]
    for i in range(11):
        m=m+[[0,0]]
    return m

def parite(c):
    p=0
    for i in range(8):
        p=(p + c) % 2
        c=c/2
    return(p)
        
def select(m,i):
    if (m[i][0] > m[i][1]):
        return(0)
    else:
        return(1)

def pselect(m,i):
    if (m[i][0] > m[i][1]):
        print 0,
    else:
        print 1,

    
def traite(s,g,n):
    m=init()
    for j in range(11):
        m[j][ord(g[j])-48]=m[j][ord(g[j])-48]+1
    for i in range(n):
        g=lit(0)
        for j in range(11):
            m[j][ord(g[j])-48]=m[j][ord(g[j])-48]+1
    c=0
    for i in range(11):
        pselect(m,i)
    for i in range(8):
        c=2*c+select(m,i+1)
    '''
    if (ord(g[8])-48) != parite(c):
        print "pbm"
    '''
    s=s+chr(c)
    print c,s
    g=lit(1)
    traite(s,g,n)

traite(s,gdeb,11)
