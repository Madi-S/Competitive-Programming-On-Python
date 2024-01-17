import time


def timeit(f):
    def inner(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        finish = time.time()
        print(f'{round(finish-start, 5)} seconds taken: {f.__name__}')
        return res
    return inner
