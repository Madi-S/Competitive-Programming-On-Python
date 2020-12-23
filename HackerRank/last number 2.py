import sys

var = ''.join([line.rstrip() for line in sys.stdin])[-1]

print(var, file = sys.stdout)