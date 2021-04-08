numeric = {'SOUTH': 1, 'NORTH': -1, 'WEST': 2, 'EAST': -2}


def dirReduc(directions):
	while True:
		reduced = False
		for i, d in enumerate(directions):
			if not i + 1 == len(directions):
				if numeric[d] + numeric[directions[i+1]] == 0:
					del directions[i: i+2]
					reduced = True
		if not reduced:
			return directions

arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))