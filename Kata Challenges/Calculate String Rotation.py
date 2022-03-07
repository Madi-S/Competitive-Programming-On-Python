def shifted_diff(first, second):
    if len(first) != len(second) or sorted(first) != sorted(second):
        return -1

    result = 0
    while first != second:
        # Move the last char to the first place, paste in remaining chars till the last char
        first = ''.join([first[-1], first[:-1]])
        result += 1
        if result >= len(first):
            return -1

    return result


def shifted_diff_2(first, second):
    if len(first) != len(second):
        return -1
    # find() return -1, if substring wasn't found
    return (second * 2).find(first)


print(shifted_diff_2('jackz', 'zjack'))
