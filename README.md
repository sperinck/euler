# Project Euler

A place to collect my solutions to Project Euler problems.

![Project Euler Badge](https://projecteuler.net/profile/sperinck.png)  
https://projecteuler.net/archives

### Problem 1: Multiples of 3 or 5
In one line of Python: `print(sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0))`  
This runs in < 0.05s. To solve by hand, we could say that the multiples of $m$ up to $n$ sum to $mT(\lfloor\frac{n}{m}\rfloor)$, where $T(k)$ is the $k$-th triangular number, and subtracting multiples of 15 to avoid double-counting, we find the answer is

$$3\cdot\frac{1}{2}(333)(334)+5\cdot\frac{1}{2}(199)(200)-15\cdot\frac{1}{2}(66)(67) = 233,168$$

### Problem 2: Even Fibonacci Numbers
Every third term after 2 is even. By letting $a_1 = a$ and $a_2 = b$, we can create a simpler sequence focusing on just these terms as $a_4 = a + 2b$ and $a_5 = 2a + 3b$. We can iterate by setting `a, b = a + 2b, 2a + 3b` - in this way, the values of $b$ are precisely the even terms.

A cheekier solution uses the fact that, on average, consecutive terms have a ratio of $\phi$, the golden ratio. To jump three terms ahead, we could multiply by $\phi^3= 2 + \sqrt{5}$. We could implement this as 

    n = 2; S = 0
    while n < 4000000: S += n; n = round(n*(2+sqrt(5)))
    print(S)

### Problem 11: Largest product in a grid
After the splitting the data up into a 20x20 matrix, the solution just runs a loop on each category of horizontal, vertical, and diagonal products, and keeps track of the largest product at any point. Runs in < 0.05s.

### Problem 12: Highly divisible triangular numbers
There are many ways to enumerate the divisors of a triangular number $T(n)$. One less efficient way is checking integers up to the square root of $T(n)$ are divisors, and then doubling the result. This works in $O(\sqrt{n})$ time, and is fine for small $n$.

For larger values of $n$, we could take inspiration from the divisor function $d(n)$. If $T(n) = p_1^{e_1}p_2^{e_2}...p_k^{e_k}$, then $d(n) = \prod_{i=1}^k (e_i+1).$
Of course, this is only useful if we can work out the prime decomposition of $T(n)$ first. This can be done with a generic isprime() function and a method for working out the multiplicities of the different primes.

The code implements this by generating the first few primes up to 100. The early triangular numbers have small prime divisors so this turns out to be enough. Amazingly, even while working out all prime multiplicities of $T(n)$, this algorithm still runs in a fraction of a second. Only small primes are being checked, but this is acceptable as the smallest highly divisible numbers will necessarily have smaller prime factors to get the biggest bang for every divisor buck. Runs in 0.1s.

### Problem 13: Large sum
Code is fairly straightforward; split the data, convert strings to integers, and sum the result. Runs in < 0.05s.
