def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = n**0.5 // 1
        f = 5
        while f <= r:
            if n % f == 0:
                return False
                break
            if n % (f+2) == 0:
                return False
                break
            f += 6
    return True

sum = 0

for n in range(1,2000000):
    if isPrime(n) == True:
        sum += n

print(sum)
