from math import sqrt
from functools import reduce


def _get_primes(n):
    pr = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            pr.add(i)
            n //= i
        else:
            i += 1
    return pr


def proper_fractions(n):
    primes = _get_primes(n)
    res = n
    for pr in primes:
        res *= (1 - (1 / pr))

    return int(res)


print(proper_fractions(100))
