def T(n):
    return n*(n+1)/2

def isPrime(n):
    if n == 1: return False
    if n < 4:  return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5 // 1)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f = f+6
    return True

def d(multiplicities): #the divisor function
    d = 1
    for i in multiplicities:
        d *= (i+1)
    return d

# Most efficient to create prime multiplicities of T(n)
# First, need a table of primes up to 100 or so.

primes = []

for n in range(1,62):
    if isPrime(n) == True:
        primes.append(n)

#print(primes)

divisors = []

for n in range(1,14000):
    N = int(T(n))
    multiplicities = []
    for p in primes:
        multiplicity = 0
        while N % p == 0:
            N /= p
            multiplicity += 1
        multiplicities.append(multiplicity)
    if d(multiplicities) > 500:
        break

print("T("+str(n)+") = "+str(int(T(n)))+" has",d(multiplicities),"divisors.")
print(primes)
print(multiplicities)

#Amazingly, this still runs in a fraction of a second. Admittedly,
#we're only checking primes up to 61, but experience shows this is
#all that's necessary as small highly divisible numbers will have
#more primes towards the lower end. So staying below 61 is efficient.
