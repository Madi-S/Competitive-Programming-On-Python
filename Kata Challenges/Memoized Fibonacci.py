

def fast_fibonacci(n, memo):
    if not n in memo:
        memo[n] = fast_fibonacci(n-1, memo) + fast_fibonacci(n-2, memo)
    return memo[n]


def fibonacci(n):
    memo = {0: 1, 1: 1}
    return fast_fibonacci(n-1, memo)


print(fibonacci(70))
