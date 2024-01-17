def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if not i % 5 and not i % 3:
            res.append('FizzBuzz')
        elif not (i % 3):
            res.append('Fizz')
        elif not (i % 5):
            res.append('Buzz')
        else:
            res.append(i)

    return res


print(fizzbuzz(4))
