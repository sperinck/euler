primes = []
for i in range(3,105000,2):
    primes.append(i)

prime_count = 1  # 2 is already accounted for

while prime_count < 10001:
    factor = primes[0]
    for n in primes:
        if n % factor == 0:
            primes.remove(n)
    prime_count += 1

print("The 10 001st prime is",factor)
