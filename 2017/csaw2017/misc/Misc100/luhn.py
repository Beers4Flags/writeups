#!/usr/bin/python

from pwn import *
import random

def somme(n):
    s=n
    while (s >=10):
        sp=0
        while (s > 0):
            sp=sp+(s%10)
            s=s/10
        s=sp
    return(s)

def luhn(n):
    r=0
    p=2
    while(n>0):
        r=r+somme((n % 10)*p)
        n=n/10
        if (p==2):
            p=1
        else:
            p=2
    return(10-(r % 10))


def generate(deb,k):
    p=deb
    for i in range(k-1):
        p=10*p+random.randint(0,9)
    p=10*p+(luhn(p)%10)
    return(p)

def test(c,s):
    return(re.match('.*'+c,s) != None)

def vluhn(n):
    return(luhn(10*n)%10)

def valide(e):
#    print "fin:",e
    ldeb=len(str(e))
#    print "ldeb=",ldeb
    l=16-len(str(e)) # longueur
    if (l %2 ==1): # cas longueur 1
        n=generate(4,l-2)
#        print "n=",n
        l=(10-luhn(n)+e)%10
#        print "l=",l
        n=(10**(ldeb+2))*n+((10-l)%10)*(10**(ldeb+1))
#        print n,e
        n=n+e
#        print n,luhn(n)
    else:
        n=generate(4,l-3)
        s=vluhn(e)%10
#        print n
        n=int(str(n)+"0"+str(s)+str(e))
    return(n)


def numero(b):
    if (test("MasterCard",b)):
#        return(generate(2221,12))
        return(generate(51,14))
    if (test("American",b)):
        return(generate(34,13))
    if (test("Bankcard",b)):
        return(generate(5610,12))
    if (test("China",b)):
        return(generate(62,14))
    if (test("nRoute",b)):
        return(generate(2014,11))
    if (test("Diners.*national",b)):
        return(generate(36,12))
    if (test("Diners",b)):
        return(generate(54,14))
    if (test("Discover",b)):
        return(generate(6011,12))
    if (test("InterPayment",b)):
        return(generate(636,13))
    if (test("InstaPayment",b)):
        return(generate(637,13))
    if (test("JCB",b)):
        return(generate(3258,16))
    if (test("Laser",b)):
        return(generate(6304,16))
    if (test("Maestro",b)):
        return(generate(50,10))
    if (test("Dankort",b)):
        return(generate(5019,12))
    if (test("MIR",b)):
        return(generate(2200,12))
    if (test("Solo",b)):
        return(generate(6334,16))
    if (test("Switch",b)):
        return(generate(4903,12))
    if (test("Visa",b)):
        return(generate(4,15))
    if (test("UATP",b)):
        return(generate(1,14))
    if (test("Verve",b)):
        return(generate(506099,10))
    if (test("TROY",b)):
        return(generate(979200,10))
    if (test("CARDGUARD",b)):
        return(generate(5392,12))
    elif (test("start",b)):
        print"TILT!!",b
        ent="starts with "
        b=b[b.index(ent)+len(ent):]
        b=b[:b.index("!")]
        return(generate(int(b),12))
    elif  (test("ends w",b)):
        ent="ends with "
        b=b[b.index(ent)+len(ent):]
        b=b[:b.index("!")]
        e=int(b)
        return(valide(e))
    else:
        ent="ed to know if "
        b=b[b.index(ent)+len(ent):]
        b=b[:b.index(" is")]
        if (vluhn(int(b))==0):
            return(1)
        else:
            return(0)
        
conn=remote('misc.chal.csaw.io', 8308)

while(1):
    b= conn.recvuntil("\n")
    print b
    while (re.match("I need",b)==None):
        b= conn.recvuntil("\n")
        print b
    n=numero(b)
    print "-->",n
    conn.sendline(str(n))

