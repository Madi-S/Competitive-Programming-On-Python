from functools import cmp_to_key


# Fill data with letters frequencies
# Filter data by exterminating letters with <= 1 frequencies
# Structure data keys by replacing letter with letters 'a' -> 'aaaaa'
# Structure data values by adding '1:', '2:' or ':='
# Sort them by frequency, then alphabetically


lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'


def descending_lexicographic_order(letter1, letter2):
    l1, l2 = letter1[2:], letter2[2:]
    if len(l1) > len(l2):
        return -1

    elif len(l1) < len(l2):
        return 1

    else:
        num1 = int(letter1[0]) if letter1[0] != '=' else 3
        num2 = int(letter2[0]) if letter2[0] != '=' else 3

        if num1 > num2:
            return 1

        elif num1 < num2:
            return -1

        else:
            if min(l1, l2) == l1:
                return -1
            return 1


def mix(s1, s2):
    print(s1 + '\n' + s2)
    data = {}

    # Fill
    for i, s in enumerate((s1, s2)):
        for letter in s:
            if letter in lowercase_letters:
                if letter in data:
                    data[letter][i] += 1
                else:
                    data[letter] = [0, 0]
                    data[letter][i] = 1

    # Filter and Structure
    res = []
    for letter, freqs in data.items():
        max_freq = max(freqs)

        if max_freq > 1:

            letter *= max_freq

            if freqs[0] > freqs[1]:
                lead = '1:'
            elif freqs[0] < freqs[1]:
                lead = '2:'
            else:
                lead = '=:'
            letter = lead + letter

            res.append(letter)
    res = '/'.join(sorted(res, key=cmp_to_key(descending_lexicographic_order)))
    return res


s1 = 'Are they here'
s2 = 'yes, they are here'


print(mix(s1, s2))


'2:eeeee/=:hh/=:rr/2:yy'
'2:eeeee/2:yy/=:hh/=:rr'
