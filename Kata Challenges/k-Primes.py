
def count_Kprimes(k, start, end):
	res = []

	for num in range(start, end + 1):
		if count_prime_divisors(num) == k:
			res.append(num)

	return res


def count_prime_divisors(n):
	res = 0
	i = 2
	while i * i <= n:
		while n % i == 0:
			n //= i
			res += 1
		i += 1

	if n > 1:
		res += 1

	return res

def puzzle(s):
	a = count_Kprimes(1, 0, s)
	b = count_Kprimes(3, 0, s)
	c = count_Kprimes(7, 0, s)
	res = 0
	for e1 in a:
		for e2 in b:
			for e3 in c:
				if (e1 + e2 + e3) == s:
					res += 1
	return res



print(count_Kprimes(2, 4, 100))

'''
k = 2  -->  4, 6, 9, 10, 14, 15, 21, 22, ...
k = 3  -->  8, 12, 18, 20, 27, 28, 30, ...
k = 5  -->  32, 48, 72, 80, 108, 112, ...

4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95
4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95
'''
