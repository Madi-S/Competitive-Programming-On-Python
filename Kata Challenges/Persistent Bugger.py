from functools import reduce
i = 0

def persistence(num):
	global i
	if num < 10:
		res, i = i, 0
		return res

	i += 1
	n = reduce(lambda a,b: int(a) * int(b), list(str(num)))
	return persistence(n)
