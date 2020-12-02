'''

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

'''

# Just count 5 and 2 pairs. Apparently, there will be 2s instead of 5s, so rather than countring 2s and 5s, just count number of 5 occurences.
# If first number is 300. Divide it by 5 and save the whole part 60 (also number of zeros must be incremented by 60).
# Then divide 60 by 5. Get 12 (increment amount of zeros by 12) and then 12 should be also divided by 5 -> 2 (increment zeros count by 2).
# Since 2 is less than 5 - we stop our calculations.


def zeros(n):
    number_of_0 = 0
    while n >= 5:
        n = n // 5
        number_of_0 += n
    return number_of_0


print(zeros(300))
