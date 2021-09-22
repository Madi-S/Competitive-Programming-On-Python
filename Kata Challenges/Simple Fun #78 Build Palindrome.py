# Just add characters from the start of the string one by one, till it is a palindrome

def build_palindrome(s):
    temp = ''

    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(s)):
        temp = s + s[0:i][::-1]
        print(temp)
        if is_palindrome(temp):
            break

    return temp


print(build_palindrome('abb'))
