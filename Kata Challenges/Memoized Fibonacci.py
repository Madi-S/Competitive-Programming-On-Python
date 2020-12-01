from sys import setrecursionlimit
setrecursionlimit(100000)


def fibonacci(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]


print(fibonacci(1000))
