import time

# Basically, Sieve of Eratosthenes is the way to find all prime numbers up to given number that > 2
# We define a step variable, which is by default 2
# Then we remove every second element starting from 2 (but step should not equal to number we remove)
# After completing it, we keep incrementing step, until it exists in the nums list
# After what we loop through again but starting from 3, we remove every step * 2 th element. E.g.: if step = 3, then delete every sixth (3*2) element, or if step = 5, then remove every tenth (5*2) element
# We keep doing this until our step (not step * 2) becomes more than square root of last number. E.g.: list up to 300 nums, we stop looping when step hits 18 


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
    if num > 2:
        step = 2
        incr = 1
        nums = [i for i in range(2, num + 1)]

        while step ** 2 < num:
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
        return [num for num in nums if isinstance(num, int)]

    return None


print(sieve_of_eratosthenes(300))
