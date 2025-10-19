def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

longest = 1

for n in range(1,1000000):
    N = n
    count = 1
    while n != 1:
        n = collatz(n)
        count += 1
    if longest < count:
        longest = count
        starting = N

print(starting)
print(longest)

#Runs in about 40 secs, not bad. Original implementation takes
#several minutes at least. Not necessary to keep track of all
#chain lengths.
