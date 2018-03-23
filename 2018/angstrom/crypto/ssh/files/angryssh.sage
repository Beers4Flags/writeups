# encoding: utf-8

import time
import base64
from Crypto.PublicKey import RSA


e = 65537
n = 24031426009258585415105324998970701655451460140660105245278171650878655493832570145520528674334486553204442446050601099312855866652174529838264749199630546148628121934849433734634042641132125007923761347962489974645002007692970466377879714666376153284839287915500514317384370204031902874952028757660051907008749997171513281852774870171717680368772057416440542176768196388565781131705261355090923059616730128088291078728643698870108958810166348296696671079733506691833466453747784418214869999275238860856569886383373280256273665811649081849561360513128165462438255912304945446909477593597880634673262567888241113884033
qh=21233617966198093532313424214919609480404030085222386232507098443793519987073202682001920049744938098606615174914582963973606467034002013094436312790321900178679115817996794763568521120660383535864330826980286862316353895425906529093977094
# on connait les 800 premiers bits soit 100 octets, il en reste 0x81-0x64=29 octets soit 232 bits
# on a donc
m=232
# q = 2^m*qh + r
ph=23759514110384115106511874493858386433869554982671790442319614656402797061682732643325894716495326858310880203542554369742113293309768983487283288116552533449101634887301003873703438670688239637524357326930108536710135761449963670522486340
# p = 2^m*qh+s
'''
n=55022099662696156434309074804848381
qh=7158444210763
ph=7158444210763
m=15
# q=234567899898288337
# p= 234567899898300013
#ph=n/qh/(2**232)/(2**232)-1
'''
def coron(pol, X, Y, k=2, debug=False):
    """
    Returns all small roots of pol.

    Applies Coron's reformulation of Coppersmith's algorithm for finding small
    integer roots of bivariate polynomials modulo an integer.

    Args:
        pol: The polynomial to find small integer roots of.
        X: Upper limit on x.
        Y: Upper limit on y.
        k: Determines size of lattice. Increase if the algorithm fails.
        debug: Turn on for debug print stuff.

    Returns:
        A list of successfully found roots [(x0,y0), ...].

    Raises:
        ValueError: If pol is not bivariate
    """

    if pol.nvariables() != 2:
        raise ValueError("pol is not bivariate")

    P.<x,y> = PolynomialRing(ZZ)
    pol = pol(x,y)

    # Handle case where pol(0,0) == 0
    xoffset = 0

    while pol(xoffset,0) == 0:
        xoffset += 1

    pol = pol(x+xoffset,y)

    # Handle case where gcd(pol(0,0),X*Y) != 1
    while gcd(pol(0,0), X) != 1:
        X = next_prime(X, proof=False)

    while gcd(pol(0,0), Y) != 1:
        Y = next_prime(Y, proof=False)

    pol = P(pol/gcd(pol.coefficients())) # seems to be helpful
    p00 = pol(0,0)
    delta = max(pol.degree(x),pol.degree(y)) # maximum degree of any variable

    W = max(abs(i) for i in pol(x*X,y*Y).coefficients())
    u = W + ((1-W) % abs(p00))
    N = u*(X*Y)^k # modulus for polynomials

    # Construct polynomials
    p00inv = inverse_mod(p00,N)
    polq = P(sum((i*p00inv % N)*j for i,j in zip(pol.coefficients(),
                                                 pol.monomials())))
    polynomials = []
    for i in range(delta+k+1):
        for j in range(delta+k+1):
            if 0 <= i <= k and 0 <= j <= k:
                polynomials.append(polq * x^i * y^j * X^(k-i) * Y^(k-j))
            else:
                polynomials.append(x^i * y^j * N)

    # Make list of monomials for matrix indices
    monomials = []
    for i in polynomials:
        for j in i.monomials():
            if j not in monomials:
                monomials.append(j)
    monomials.sort()

    # Construct lattice spanned by polynomials with xX and yY
    L = matrix(ZZ,len(monomials))
    for i in range(len(monomials)):
        for j in range(len(monomials)):
            L[i,j] = polynomials[i](X*x,Y*y).monomial_coefficient(monomials[j])

    # makes lattice upper triangular
    # probably not needed, but it makes debug output pretty
    L = matrix(ZZ,sorted(L,reverse=True))

    if debug:
        print "Bitlengths of matrix elements (before reduction):"
        print L.apply_map(lambda x: x.nbits()).str()

    L = L.LLL()

    if debug:
        print "Bitlengths of matrix elements (after reduction):"
        print L.apply_map(lambda x: x.nbits()).str()

    roots = []

    for i in range(L.nrows()):
        if debug:
            print "Trying row %d" % i

        # i'th row converted to polynomial dividing out X and Y
        pol2 = P(sum(map(mul, zip(L[i],monomials)))(x/X,y/Y))

        r = pol.resultant(pol2, y)

        if r.is_constant(): # not independent
            continue

        for x0, _ in r.univariate_polynomial().roots():
            if x0-xoffset in [i[0] for i in roots]:
                continue
            if debug:
                print "Potential x0:",x0
            for y0, _ in pol(x0,y).univariate_polynomial().roots():
                if debug:
                    print "Potential y0:",y0
                if (x0-xoffset,y0) not in roots and pol(x0,y0) == 0:
                    roots.append((x0-xoffset,y0))
    return roots


def egcd(a,b):
    '''
    Extended Euclidean Algorithm
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

def modInverse(e,n):
    return egcd(e,n)[0]%n

def racineimpair(x,m):
    if (m <= 3):
        if (x==1):
            return(1)
        else:
            return(-1)
    mp=8
    c=3
    y=x % 8
    if (y != 1):
        return(-1)
    r=1
    while (c < m):
        c=c+1
        mp=mp*2
        if ((((r * r) - x) % mp) != 0):
            r=r+(mp/4)
    return(r)



def logdeux(x):
    r=0
    while(x % 2 == 0):
        r+=1
        x=x/2
    return(r)

def racine(x,g):
    m=logdeux(x)
    if (g <= m):
        return([(2**((g+1)/2))*k for k in range(2**(g/2))])
    if (m % 2 == 1):
        return[]
    if (g==m+1):
        return([(2**((m/2)+1))*k + 2**(m/2) for k in range(2**(m/2-1))])
    if (g==m+2):
        return([(2**((m/2)+2))*k + 2**(m/2) for k in range(2**(g/2))]+[(2**((m/2)+2))*k - 2**(m/2) for k in range(2**(m/2-2))])
    y=x/(2**m)
    if not ((y % 8) == 1):
        return[]
    r=racineimpair(y,g-m)
    l1=[2**(m/2)*r+k*2**(g-(m/2)) for k in range(2**(m/2))]
    l2=[-2**(m/2)*r+k*2**(g-(m/2)) + 2**g for k in range(2**(m/2))]
    l3=[2**(m/2)*(r+2**(g-m-1))+k*2**(g-(m/2)) for k in range(2**(m/2))]
    l4=[2**(m/2)*(-r+2**(g-m-1))+k*2**(g-(m/2)) for k in range(2**(m/2))]
    return(l1+l2+l3+l4)


'''
(2*ph*2^m + x)*(qh*2^m +y ) = n

soit ph*qh*2^(2*m) +x*y + ph*2^m*y + qh*2^m*y = n

avec x et y en  m^(1/2) = (m^2)^0.25


'''
mm=2**m


P.<x,y> = PolynomialRing(ZZ)

pol=(ph*mm+x)*(qh*mm+y) -n
X=mm
Y=mm

sol = coron(pol, X, Y, k=2, debug=False)
if (len(sol)>0):
        solx,soly=sol[0]
        print "solx=",solx
        print "soly=",soly
	pp=ph*mm+solx
	qq=qh*mm+soly
	print pp,qq,pp*qq-n


print "p=",pp
print "q=",qq
print "n=",n
print "e=",e
Zphi=Zmod((pp-1)*(qq-1))

d=int(1/Zphi(e))*1L
print "d=",d
print "1=",(e*d % ((pp-1)*(qq-1)))
exit(0)

key=RSA.construct([n,e*1L,d,pp,qq])

f = open('privkey.pem','w')
f.write(key.exportKey('PEM'))
f.close()

'''
102
103
104
105
pp= 6240417853421707582709427962158555962984114118507379146186852539727310928576327553685301555077616930971137098036275856785346221116682427824328775461139123213363290212283738106654524067430367241346181318541347183917645235338100231263996283802653479268892457704896413693295613386583617583325048460570925961530182904686344192364889651328465294813521918403980768019995652460161889426627419671717571471012943786827672434377523
qq= 6835364876775996029897770662037941385323593294440860405171263071653191152980983524117461985490587562500416651600220265368038713587848500304014198950218174253359790321073915774732551210576337631777854719124222034607381244034902329652565797805547044046433659790970367988355060012090220538173584049920375620162180544137306472928549459445942033295103401750345916196778761513834862228748545320261802902622647593201339619023157
mm= 6917257425689530036622985546718721032458048899171898480735288332161153759265304724368239531227090326307349383041499823466971386343244651801294157545363169233480268460307612535996044740389512799159954588308125393833558110056091314603315306137267161874183473373214673459734004841723514031219907235701547001390855970990191853377446857678811103668220504652391954935598744989572362036837653935170399380502807145490246317113344
solx= 3767000340817111041342911265905304597760136201537269994370315722397929857901078600733297585239742449430962420582272594632435492512077728135725899069041249005007692465266795673248487600969754944646
soly= 4268027375033179183431185942652641578717486035804474137278301515875600821331466665707788031889238764488825709575177446684358316386024543670749009584052942549014852819180886559367148115385004886059
106
107
108
'''

exit(0)
