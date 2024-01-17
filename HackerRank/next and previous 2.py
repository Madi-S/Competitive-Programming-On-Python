import sys


a = int(sys.stdin.read().strip())

print(f'The next number for the number {a} is {a + 1} \
    .\nThe previous number for the number {a} is {a - 1}.', file=sys.stdout)
