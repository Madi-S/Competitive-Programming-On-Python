import sys


a = int(sys.stdin.read().strip())

print(sum([i for i in range(1, a + 1)]), file=sys.stdout)
