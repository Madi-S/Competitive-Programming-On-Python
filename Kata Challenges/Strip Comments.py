
'''

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

'''


def solution(string, markers):
    rows = string.split('\n')
    res = []
    for row in rows:
        a = ''
        for i in range(len(row)):
            if row[i] in markers:
                break
            a += row[i]

        a = a.strip()
        res.append(a)

    return '\n'.join(res)


print(
    solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))

# 'apples, pears \ngrapes\nbananas'
# 'apples, pears\ngrapes\nbananas'
