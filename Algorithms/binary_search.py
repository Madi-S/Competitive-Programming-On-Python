# Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
# Begin with an interval covering the whole array.
# If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
from timeitf import timeit


@timeit
def binary_search(nums, n):
    nums.sort()

    lower_bound, upper_bound = 0, len(nums) - 1

    while lower_bound <= upper_bound:
        mid_bound = (lower_bound + upper_bound) // 2
        mid_value = nums[mid_bound]

        print(n, mid_value)

        if n == mid_value:
            print(f'Match: {n} at {mid_bound}')
            return True

        elif n > mid_value:
            lower_bound = mid_bound + 1

        else:
            upper_bound = mid_bound - 1

    return False


binary_search([123, 345, 123123, 542, 76, 0, 1233], 123123)
assert binary_search(list(range(123, 300, 5)), 193)
assert binary_search(list(range(353, 9943, 12)), 8323) == False
