import sys

a = sys.stdin.read().split('\n')
a = 'YES' if a[0] in a[2:] or a[1] in a[2:] else 'NO'

print(a, file = sys.stdout)