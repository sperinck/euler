a = 1; b = 2; S = 0
while b < 4000000:
	S += b
	a, b = a + 2*b, 2*a + 3*b
print(S)
