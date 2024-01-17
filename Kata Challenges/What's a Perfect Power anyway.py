from math import log


def isPP(n):
    if n < 0:
        return None
    for i in range(2, 100000):
        power = round(log(n, i) + 0.00000000000001, 6)
        if power == int(power) and power > 1:
            return [i, int(power)]
    return None


print(isPP(243))
print(log(243, 3))
