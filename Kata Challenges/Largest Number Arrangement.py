from time import time
from itertools import permutations


def largest_arrangement_1(numbers):
    res = ''
    digits = {}

    for num in numbers:
        digit = str(num)[0]
        if digit in digits:
            digits[digit].append(num)
        else:
            digits[digit] = [num, ]

    for digit in sorted(list(digits.keys()), reverse=True):
        nums_len = [[num, len(str(num))] for num in digits[digit]]
        max_len = len(str(max(digits[digit])))

        for i, num_len in enumerate(nums_len):
            filled_num = str(num_len[0])
            while len(filled_num) < max_len:
                filled_num += filled_num

            nums_len[i][0] = filled_num

        for num, length in sorted(nums_len, reverse=True):
            res += str(num)[:length]

    return int(res)


def largest_arrangement_2(numbers):
    return max(int(''.join(p)) for p in permutations(map(str, numbers)))


args = (
    [7, 78, 79, 72, 709, 7, 94],
    [8, 6, 590, 70],
    [6, 73, 79, 356, 7],
    [64, 29, 5, 9, 982, 3],
    [3487, 103559, 243],
    [7, 78, 79, 72, 709, 7, 94],
)


start = time()
for _ in range(1000):
    for arg in args:
        largest_arrangement_1(arg)
print(time() - start)


start = time()
for _ in range(1000):
    for arg in args:
        largest_arrangement_2(arg)
print(time() - start)


# Low-level solution #1 is much better that using permutations in solution #2
# 1 func: 0.1189265251159668 sec
# 2 func: 6.754024982452393  sec
