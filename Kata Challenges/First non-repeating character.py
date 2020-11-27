'''

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

'''


def first_non_repeating_letter(string):
    res = list(map(lambda s: s.upper() if s.isupper() else s.lower(), string))
    counter = {}
    for letter in res:
        if letter.upper() in counter:
            counter[letter.upper()] += 1
        elif letter.lower() in counter:
            counter[letter.lower()] += 1
        else:
            counter.update({letter: 1})
    for l, c in counter.items():
        if c == 1:
            print(l)
            return l
    return ''


# loop through the string append all unique letters with their count
first_non_repeating_letter('hello world, eh?')
