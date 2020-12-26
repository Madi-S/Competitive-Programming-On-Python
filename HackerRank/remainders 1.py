import sys

a = sys.stdin.read().strip().split('\n')
a, b, r, d = int(a[0]), int(a[1]), int(a[2]), int(a[3]) 
nums = [i for i in range(a, b + 1) if i % d == r]
print(*nums, file = sys.stdout)