import sys


a = 'YES' if int(sys.stdin.read().strip()) % 2 == 0 else 'NO'

print(a, file=sys.stdout)
