def primes():
    MAX = 16000000 - 1
    SQ = int(MAX ** (1 / 2) + 1)
    arr = [False] + [True] * MAX
    for i in range(3, SQ, 2):
        if arr[i]:
            arr[i * i::2 * i] = [False]*(((MAX - (i * i)) // (2 * i)) + 1)
    return [2] + [i for i in range(3, MAX, 2) if arr[i]]


class Primes:
    li = primes()

    @staticmethod
    def stream():
        yield from Primes.li
