# Project Euler

A place to collect my solutions to Project Euler problems.

![Project Euler Badge](https://projecteuler.net/profile/sperinck.png)  
https://projecteuler.net/archives

### Problem 1: Multiples of 3 or 5
The one-line iterative summation in `euler1.py` runs in < 0.05s. To solve by hand, we could note that the multiples of $k$ up to $999$ sum to $k \times T\Big(\big[\frac{999}{k}\big]\Big)$, where $T(n)$ is the $n$-th triangular number. Removing duplicates, we find the sum to be

$$3\cdot\frac{1}{2}(333)(334)+5\cdot\frac{1}{2}(199)(200)-15\cdot\frac{1}{2}(66)(67) = 233,168$$

### Problem 2: Even Fibonacci Numbers
$(a)$ Every third term after 2 is even. By letting $a_1 = a$ and $a_2 = b$, we can create a simpler sequence focusing on just these terms by using $a_4 = a + 2b$ and $a_5 = 2a + 3b$. We can iterate by setting `a, b = a + 2b, 2a + 3b` $-$ in this way, the values of $b$ are precisely the even terms.

$(b)$ A lazier solution uses the fact that, on average, consecutive terms have a ratio of $\phi$, the golden ratio. To jump three terms ahead, we could multiply by $\phi^3= 2 + \sqrt{5}$. We could implement this as a sum of the sequence $a_n$ such that $a_0 = 2$ and $a_{n+1} = \text{round}(2+\sqrt{5})a_n$ while $a_n$ < 4 million.

### Problem 3: Largest Prime Factor
My original solution was to compile a list of primes to test against $-$ workable but very inefficient. Far better to completely divide out the big evil number $n$ by each natural number $2,3,4,5...$, making the number smaller at each step until we have $n=1$, as in the overview to problem 3. This is a thousand times faster than compiling primes. Even this can be improved by only considering odd numbers after 2.

### Problem 4: Largest Palindrome Product
A bit of wishful thinking goes a long way. We can avoid a lot of iteration by only checking products $m\times n$ where $m$ and $n$ are larger than $900$. That gives $5000$ cases to check, if we ignore duplicates. I can't prove that the largest palindrome will occur in this region, or how this might be generalised, but the answer works in any case.

### Problem 5: Smallest Multiple
This can be done by hand, though a pocket calculator helps with the last step. First, the primes: $2\times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19$. Under $20$, the highest powers of $2$ and $3$ are $2^4$ and $3^2$ respectively. Including these in the product gives the answer.

### Problem 6: Sum Square Difference
A-level mathematicians live for this sort of question (or they should!). The required value, where $n=100$, is:

$$
\\begin{align*}
\bigg( \sum_{k=1}^{n} k \bigg)^2 - \sum_{k=1}^{n} k^2 &= \frac{1}{4}n^2(n+1)^2 - \frac{1}{6}n(n+1)(2n+1) \\\\
&= \frac{1}{12}n(n+1)[3n(n+1)-2(2n+1)] \\\\
&= \frac{1}{12}n(n+1)(3n^2-n-2)
\\end{align*}
$$

We can verify this with the value given in the problem when $n=10$.

### Problem 7: 10 001st Prime
Using the famous [prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem), where $\pi(x)$ is the prime-counting function, we see that $\pi(10^5) \approx 8686$ and $\pi(2\times 10^5) \approx 16385$, so we might expect the 10 001st prime to be a little higher than 100 000.

The code in the solution works by using the Sieve of Eratosthenes. It takes the first prime 2 as given, and generates an array of the odd numbers from 3 to 110 000. Then it removes all multiples of 3 (including 3), all multiples of 5 (including 5), and so on, so that the first number in the array is always the next prime to be considered, adding one to `prime_count` at each stage until the 10 001st prime is found.

Note: 110 000 was not the first number I tried! But there are enough clues from the PNT to guess it might be something in this region.

### Problem 8: Largest Product in a Series
Once the big number is encoded $-$ easier said than done! though with only 20 lines I went for the labour-intensive way here $-$ it is easy enough to create strings of length 13, convert into integers and find their product. One can keep track of all 988 products or disregard those that are not statistically big enough.

What counts as not big enough, you say? Doing it neatly would take far too long, but heuristically, there are $10^{13}$ possibilities for thirteen-digit numbers containing the digits $0$ to $9$; of those, there are $10^{10}$ that have three 9s at the beginning. So a number containing three 9s (not accounting for permutations) is _roughly_ in the top 0.1%. Then a very hand-wavy average choice of $9\times 9 \times 9 \times 5^{10}$ gives the top 0.1% as sitting somewhere in the region of $7\times 10^9$. It turns out that 4 such products are in this region: not a bad estimate, though a little less than the 10 or so we'd expect $-$ but then again, this argument is about as concrete as wet lettuce.

### Problem 9: Special Pythagorean Triplet
Happily this is another that can be done entirely by hand. It can be shown that, given any positive integers $u, v$ where $u > v$, the numbers $x = 2uv$, $y = u^2 - v^2$, and $z = u^2+v^2$ form a Pythagorean triple (the converse is also true: given any Pythagorean triple $(x,y,z)$ there exist positive integers $u, v$ such that these relations hold). Though it is not important for this question, it's interesting to note that the Pythagorean triple has no common factors (i.e. is _primitive_) if and only if $u, v$ are coprime with opposite parity.

We are looking, then, for the solution to:

$$
\\begin{align*}
x+y+z &= 1000 \\\\
2uv + (u^2-v^2)+(u^2+v^2) &= 1000 \\\\
2u^2 + 2uv &= 1000 \\\\
u(u+v) &= 500
\\end{align*}
$$

As $0<v<u$ it follows that $u<u+v<2u$, so we are looking for a pair of factors whose ratio is less than 2, which limits the search considerably. There is only one pair of factors that satisfies this, namely 20 and 25. These give $x = 200$, $y = 375$, and $z = 425$. Their product can be worked out by hand by using the difference of two squares:

$$
200\times (400-25) (400+25) = 200 \times (160,000 -625) = 32,000,000 - 125,000 = 31,875,000
$$

### Problem 10: Summation of Primes
Though it summed all the primes up to two million in under a minute, my first primality checker was not as efficient as the one used in the 'official' solution to 7, which is what `euler10.py` is based on. That algorithm takes seconds to run, though anything over a few million might stretch it to its limits.

### Problem 11: Largest product in a grid
After the splitting the data up into a 20x20 matrix, the solution just runs a loop on each category of horizontal, vertical, and diagonal products, and keeps track of the largest product at any point. Runs in < 0.05s.

### Problem 12: Highly divisible triangular numbers
There are many ways to enumerate the divisors of a triangular number $T(n)$. One less efficient way is checking integers up to the square root of $T(n)$ are divisors, and then doubling the result. This works in $O(\sqrt{n})$ time, and is fine for small $n$.

For larger values of $n$, we could take inspiration from the divisor function $d(n)$. If $T(n) = p_1^{e_1}p_2^{e_2}...p_k^{e_k}$, then $d(n) = \prod_{i=1}^k (e_i+1).$
Of course, this is only useful if we can work out the prime decomposition of $T(n)$ first. This can be done with a generic isprime() function and a method for working out the multiplicities of the different primes.

The code implements this by generating the first few primes up to 100. The early triangular numbers have small prime divisors so this turns out to be enough. Amazingly, even while working out all prime multiplicities of $T(n)$, this algorithm still runs in a fraction of a second. Only small primes are being checked, but this is acceptable as the smallest highly divisible numbers will necessarily have smaller prime factors to get the biggest bang for every divisor buck. Runs in 0.1s.

### Problem 13: Large sum
Code is fairly straightforward; split the data, convert strings to integers, and sum the result. Runs in < 0.05s.
