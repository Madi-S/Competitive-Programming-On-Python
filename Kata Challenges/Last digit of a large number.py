powers = {
	0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1], 
}

def last_digit_1(n1, n2):
	if n2 == 0:
		return 1

	n1_last = int(str(n1)[-1])
	power = powers[n1_last]

	return power[n2 % 4 - 1]


def last_digit_2(n1, n2):
	return pow(n1, n2, 10)