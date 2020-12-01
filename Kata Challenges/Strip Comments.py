

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
