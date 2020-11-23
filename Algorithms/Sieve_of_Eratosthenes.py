import time
from math import ceil, sqrt


def timeit(f):
    def inner(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        finish = time.time()
        print(f'{round(finish-start, 5)} seconds taken: {f.__name__}')
        return res
    return inner


@timeit
def sieve_of_eratosthenes(num):
    step = 2
    incr = 1
    nums = [i for i in range(2, num + 1)]

    while step ** 2 - 1 <= num:
        print(step)
        for index in range(step - 2, num - 1, step * incr):
            if step - index != 2 and isinstance(nums[index], int):
                print(
                    f'{nums[index]} is divisible by {step}, at postion: {index}')
                nums[index] = 'Not Prime'

        step += 1
        while True:
            if not step in nums:
                step += 1
                print(f'Step incremented to {step}')
            else:
                break

        incr = 2

    print(nums)


sieve_of_eratosthenes(200)
