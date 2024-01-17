def sum_pairs(ints, s):
    if sum(ints) < s:
        return None

    i, j, k = 0, 1, 2

    while k <= len(ints):
        int1 = ints[i]
        int2 = ints[j]

        if int1 + int2 == s:
            print([int1, int2])
            return [int1, int2]
            break

        i += 1
        j += 1
        print(i, j)

        if j == len(ints):
            print('incr', k)
            i = 0
            j = k
            k += 1

    print('nothing')
    return None


sum_pairs([4, -2, 3, 3, 4], 8)
