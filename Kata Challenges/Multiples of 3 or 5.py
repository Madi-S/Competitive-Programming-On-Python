def solution(num):
    res = 0
    for i in range(3, num):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res
