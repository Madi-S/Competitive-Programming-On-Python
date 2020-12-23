import sys

k,r,f = ''.join([line.rstrip() for line in sys.stdin]).split(' ')
sum_ = 5 * int(r) + 3 * int(k) + 12 * int(f)
print(sum_, file = sys.stdout)