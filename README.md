# Project Euler

https://projecteuler.net/archives

### Problem 11: Largest product in a grid
After the splitting the data up into a 20x20 matrix, the solution just runs a loop on each category of horizontal, vertical, and diagonal products, and keeps track of the largest product at any point. Runs in < 0.05s.

### Problem 12: Highly divisible triangular numbers
There are many ways to enumerate the divisors of a triangular number $T(n)$. One less efficient way is checking integers up to the square root of $T(n)$ are divisors, and then doubling the result. This works in $O(\sqrt{n})$ time, and is fine for small $n$.

For larger values of $n$, we could take inspiration from the divisor function $d(n)$. If $T(n) = p_1^{e_1}p_2^{e_2}...p_k^{e_k}$, then $d(n) = \prod_{i=1}^k (e_i+1).$
Of course, this is only useful if we can work out the prime decomposition of $T(n)$ first. This can be done with a generic isprime() function and a method for working out the multiplicities of the different primes.

The code implements this by generating the first few primes up to 100. The early triangular numbers have small prime divisors so this turns out to be enough. Amazingly, even while working out all prime multiplicities of $T(n)$, this algorithm still runs in a fraction of a second. Only small primes are being checked, but this is acceptable as the smallest highly divisible numbers will necessarily have smaller prime factors to get the biggest bang for every divisor buck. Runs in 0.1s.

### Problem 13: Large sum
Code is fairly straightforward; split the data, convert strings to integers, and sum the result. Runs in < 0.05s.
