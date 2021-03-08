kn = '5'
k = ['2', '7', '3', '4', '8']

qn = '3'
q = [['1', '1', '3'], ['2', '4', '6'], ['1', '1', '5']]

# kn = input()
# k = input().split(' ')
# qn = input()

res = 0

for i in range(int(qn)):
    a = input().split(' ')
    if a[0] == '1':
        res += sum([int(l) for l in k[int(a[1]) - 1: int(a[2])]])
    else:
        k[int(a[1]) - 1] = int(a[2])

print(res)


'''
5
2 7 3 4 8
3
1 1 3
2 4 6
1 1 5
'''

# 5 [2, 7, 3, 4, 8] 3 [[1, 1, 3], [2, 4, 6], [1, 1, 5]]
