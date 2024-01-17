'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''


# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
def solution(nums):
    # compare two numbers
    # if they are in range respectively -> add to buffer
    # else -> add first and last nums of buffer to res and clear buffer and add current num to res

    # if buffer exists and equilibrium fails -> add current to buffer and clear buffer
    # nums.append(999)
    buff = []
    res = []

    for i, num in enumerate(nums):
        if i + 1 != len(nums) and num + 1 == nums[i+1]:
            if num + 1 == nums[i+1]:
                buff.append(num)
        else:
            if buff:
                buff.append(num)
                if len(buff) >= 3:
                    res.append(f'{buff[0]}-{buff[-1]}')
                else:
                    for num in buff:
                        res.append(str(num))
                buff.clear()
            else:
                res.append(str(num))

    return ','.join(res)


# assert solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5,
      7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
