'''

There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. 
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce
the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

'''


def recoverSecret(triplets):
	'triplets is a list of triplets from the secrent string. Return the string.'
	secret=[]
	for a in triplets:
	    x = a[0]
	    y = a[1]
	    z = a[2]
	    if x not in secret:
	        secret.insert(0,x)
	    if y not in secret:
	        secret.insert(secret.index(x) + 1,y)
	    if y in secret and secret.index(y) < secret.index(x):
	        secret.pop(secret.index(y))
	        secret.insert(secret.index(x) + 1, y)
	    if z not in secret:
	        secret.insert(secret.index(y) + 1,z)
	    if z in secret and secret.index(z) < secret.index(y):
	        secret.pop(secret.index(z))
	        secret.insert(secret.index(y) + 1, z)
	return ''.join(secret)

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]


print(recoverSecret(triplets))