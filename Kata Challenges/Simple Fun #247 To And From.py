def to_and_from(a, b, t):
    length = b - a

    if t >= length:
        cycles = t // length
        reamining = t - length * cycles

        if cycles % 2 == 0:
            return reamining + a
        else:
            return b - reamining

    return t + a

    '''
    A = 5
    B = 25
    t = 52
    
    length = 25 - 5 = 20
    cycles = 52 // 20 = 2
    remaining = 52 - 2 * 20 = 12
    
    if cycles is divisible by 2 (start from A):
        result = reamining + a
    if cycles is NOT divisible by 2 (start from B):
        result = b - remaining

    if t is less than length:
        result = a + t
        because we starting from a
    '''
