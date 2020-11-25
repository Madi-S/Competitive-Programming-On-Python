# Pythonic way to reverse a list without [::-1] or reverse() method
from timeitf import timeit


@timeit
def reverse(seq):
    # Take simmetric values and swap them

    for i in range(len(seq) // 2):
        simmetric = len(seq) - 1 - i    # or -i - 1
        seq[i], seq[simmetric] = seq[simmetric], seq[i]

    print(seq)


print(reverse([3, 4, 5, 6, 7, 8, 9, 10, 11]))
