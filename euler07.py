primes = []
for i in range(3,105000,2):
    primes.append(i)

for p in primes:
    for n in primes:
        if n == p:
            continue
        elif n % p == 0:
            primes.remove(n)

print(primes[9999])
