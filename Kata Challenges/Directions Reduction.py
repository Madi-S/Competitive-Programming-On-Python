numeric = {'SOUTH': 1, 'NORTH': -1, 'WEST': 2, 'EAST': -2}


def dirReduc(directions):
	while True:
		reduced = False
		print('^Before:',directions)
		for i, d in enumerate(directions):
			if not i + 1 == len(directions):
				# if (d == 'NORTH' and directions[i+1] == 'SOUTH') or \
				#  (d == 'SOUTH' and directions[i+1] == 'NORTH') or \
				#  (d == 'WEST' and directions[i+1] == 'EAST') or \
				#  (d == 'EAST' and directions[i+1] == 'WEST'):
				if numeric[d] + numeric[directions[i+1]] == 0:
					print(f'?Deleting: {directions[i]} at {i} {directions[i+1]} at {i+1}')
					del directions[i: i+2]
					print(f'!After deletion: {directions}')
					reduced = True
		if not reduced:
			return directions

arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))