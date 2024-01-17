trib = []


def tribonacci(
    signature,
    n,
    last_three
):
    global trib

    if not trib:
        trib = signature

    if not last_three:
        last_three = signature

    if n <= len(trib):
        print('Triggered', trib[-n:], trib)
        return trib[-n:]

    last_first = last_three[-1]
    last_second = last_three[-2]
    last_third = last_three[-3]

    first = last_first + last_second + last_third

    second = first + last_first + last_second

    third = second + first + last_first

    last_three = (first, second, third)
    trib.extend(last_three)

    tribonacci(signature, n, last_three)


print(tribonacci([0, 1, 1], 20, None))
