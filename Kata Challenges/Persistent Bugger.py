from functools import reduce


def persistence(num):
    if num < 10:
        return 0

    n = reduce(lambda a, b: int(a) * int(b), list(str(num)))
    return persistence(n) + 1
