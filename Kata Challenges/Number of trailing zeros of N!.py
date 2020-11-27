'''

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

'''


def zeros(n):
    number_of_0 = 0
    while n >= 5:
        n = n // 5
        number_of_0 += n
    return number_of_0

print(zeros(1123))
