'''

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

'''


def solution(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            try:
                result.append(s[i] + s[i+1])
            except:
                result.append(s[i] + '_')

    return result


assert solution('asdfadsf') == ['as', 'df', 'ad', 'sf']
assert solution('asdfads') == ['as', 'df', 'ad', 's_']

'''

test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
    
'''
