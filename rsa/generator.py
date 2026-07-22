import secrets
import random
from rsa.constants import First_85_Primes, PUBLIC_EXPONENT

def nBitrandom(n):
    rand_int = secrets.randbits(n)
    # forcing the 1024th bit to 1
    rand_int |= (1 << (n-1))
    rand_int |=1                # forcing the number to be a odd number
    return rand_int

def low_level_primality_test():
    while True:
        num = nBitrandom(1024)
        for divisor in First_85_Primes:
            if divisor*divisor > num:
                break
            if num%divisor == 0:
                break
            
        else:
            return num

        
def isRabinMillerPassed(n):
    m= n-1
    k=0
    while m%2==0:
        m//=2
        k+=1

    for _ in range(20):
        a=random.randrange(2, n-1)
        b=pow(a,m,n)

        if b==1 or b == n-1:
            continue

        for _ in range(k-1):
            b=pow(b,2,n)
            if b==n-1:
                break
        else:
            return False
    return True

def getPrime():
    while True:
        num=low_level_primality_test()
        if not isRabinMillerPassed(num):
            continue   
        else:
            return num


def extended_euclidean_algorithm(e,phi_n):
    a,b = phi_n,e
    t1,t2 = 0,1     # initial values
    while b>0:
        q=a//b
        t= t1 - (t2*q)
        r = a%b
        a,b,t1,t2=b,r,t2,t

    return t1 % phi_n   # this %phi_n avoids any negative value by replacing it with it's mathematical inverse

def generate_KeyPair():
    p = getPrime()
    q = getPrime()
    n = p*q
    phi_n = (p-1)*(q-1)
    e=PUBLIC_EXPONENT
    d=extended_euclidean_algorithm(e,phi_n)

    if (e*d)%phi_n!=1:
        raise ValueError("Fatal Error during Private Key Generation")

    return (e,n),(d,n) # returns (publickey, privatekey)

