def solution(num):
	if number < 0:
		return 0
	res = []
	for i in range(3, num+1):
		if i % 3 == 0 or i % 5 == 0:
			res.append(i)
	return res