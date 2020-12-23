import sys

a = int(sys.stdin.read().strip())
if a > 0:
	a = 1
elif a < 0:
	a = -1
else:
	a = 0
print(a, file = sys.stdout)