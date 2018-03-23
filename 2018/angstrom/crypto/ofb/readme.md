# [CTF ANGSTROM] Write-Up - OFB (Crypto, 120)

## Description :
Un fichier flag.png est chiffrée avec une clef de la façon suivante: chaque bloc de 4 octets est «xorisé» à une clef obtenue par une suite
x(0) = x0 initial
x(n+1)= a*x(n) + c % m

(m = 2**32)

a,c et x0 sont inconnus


## Résolution.

Le fichier commence par

89 50 4E 47  0D 0A 1A 0A  00 00 00 0D

ce qui permet d'avoir les 3 premières valeurs de la suite x(n). À partir de cela, on peut retrouver a, c et x0 et en déduire la suite complète ce qui permet de déchiffrer complètement le fichier.

Programme python:

```PYTHON
import struct

def egcd(a,b):
    '''
    returns x, y, gcd(a,b) such that ax + by = gcd(a,b)
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a

def chinois(a,b,ma,mb):
    '''
    Resout n=ma%a et m=mb%b
    '''
    u,v,d=egcd(a,b)
    sol=(mb-ma)*u*a+ma
    p=a*b
    if (sol < 0):
        sol+=p*(1-(sol//p))
    return(sol %(a*b))
    
def modInverse(e,n):
    '''
    d such that de = 1 (mod n)
    e must be coprime to n
    this is assumed to be true
    '''
    return egcd(e,n)[0]%n

def lcg(m, a, c, x):
	return (a*x + c) % m


def stow(s):
    return(struct.unpack('>I', s)[0])

def wtos(n):
    return(struct.pack('>I', n))

def divise(u,v,m):
    d=gcd(v,m)
    print "gcd=",d
    w=modInverse(v/d,m/d)
    r=(u*w) % (m/d)
    return([r+k*(m/d) for k in range(d)])


m = pow(2, 32)

e = open('flag.png.enc').read()
e = [e[i:i+4] for i in range(0, len(e), 4)]

debut="\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"
en=e
deb=[]
i=0
while(i+4<=len(debut)):
    deb=deb+[debut[i:i+4]]
    i=i+4

y0 = stow(en[0])^stow(deb[0])
y1 = stow(en[1])^stow(deb[1])
y2 = stow(en[2])^stow(deb[2])

la=divise((y2-y1+m) %m,(y1-y0+m)%m,m)
for a in la:
    b= (y2 + (m- a)*y1) % m
    print "a=",a
    print "b=",b
    print "# ----"

a=la[0]    
b= (y2 + (m- a)*y1) % m
    
y=y0
dl = []
for i in range(len(e)):
    car=wtos(y^stow(e[i]))
    dl = dl+[car]
    y=lcg(m, a, b, y)

d=''
for s in dl:
    d=d+s
f=open("flag.png","wb")
f.write(d)
f.close()
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
