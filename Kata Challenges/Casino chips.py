import math


def solve(arr):
    a, b, c = arr
    min_ = min(a + b, b + c, c + a, math.floor(a + b + c) / 2)
    days = math.floor(min_)
    return days


if __name__ == '__main__':
    print(solve([12, 12, 12]))
