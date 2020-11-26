import time


def find(N):
    def check_reversed(num: str):
        for n in range(len(num) // 2):
            if num[n] != num[-n-1]:
                return False

        return True

    a = (0, 0)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not i == j:
                if check_reversed(str(i * j)):
                    a = (i, j)          # First goes the smallest number

    return (min(a), max(a))


start = time.time()
print(find(1000))
print(time.time() - start)
