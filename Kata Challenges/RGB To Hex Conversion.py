def rgb(r, g ,b):
	res = ''
	for color in (r, g, b):
		if color > 255:
			color = 255
		elif color < 0:
			color = 0

		clr = hex(color)[2:]
		while len(clr) < 2:
			clr = '0' + clr 
		res += clr

	return res.upper()

print(rgb(1, 2, 3))