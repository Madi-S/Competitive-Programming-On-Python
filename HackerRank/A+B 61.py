import sys


nums = [int(line.rstrip()) for line in sys.stdin]

print(sum(nums), file=sys.stdout)
