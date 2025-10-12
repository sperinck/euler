largest = 1
for m in range(900,1000):
    for n in range(m,1000):
        if m*n == int(str(m*n)[::-1]) and largest < m*n:
            largest = m*n
print(largest)
