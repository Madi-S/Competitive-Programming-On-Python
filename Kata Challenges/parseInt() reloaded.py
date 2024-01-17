'''
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''


a = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
b = {'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
     'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
c = {'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
     'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}


def parse_under_100(string):
    if '-' in string:
        string = string.split('-')
        return b[string[0]] + a[string[1]]

    elif string in list(a.keys()):
        print(string, '<= 9')
        return a[string]

    elif string in list(b.keys()):
        print(string, '<= 99')
        return b[string]

    else:
        print(string, '<= 19')
        return c[string]


def parse_int(string):
    print(string)
    if string == 'one million':
        return 1000000

    string = string.replace(' and', '').split(' ')
    integer = 0
    nums = []

    if len(string) < 2:
        return parse_under_100(string[0])

    for s in string:
        if not (s.startswith('hund') or s.startswith('thou')):
            nums.append(parse_under_100(s))
        else:
            nums.append(s)

    print('intial', nums)

    # Parsing 1-99 number
    if isinstance(nums[-1], int):
        integer += nums.pop(-1)
        print('first', integer)

    # Parsing first hundred or returning number not containing hundreds
    last = nums[-1]
    if isinstance(last, str):
        i = 0

        if last.startswith('h'):
            i = 100
        elif last.startswith('t') and len(nums) == 1:
            i = 1000
        elif last.startswith('t') and isinstance(nums[-2], str):
            integer += 100000 * nums.pop(0)
            return integer

        if i:
            nums.pop(-1)
            integer += i * nums.pop(-1)

    print('second', integer)

    if nums:
        # [7, 'hundred', 83, 'thousand']	798
        print(nums)

        if 'hund' in str(nums):
            if len(nums) == 4:
                i = nums[2]
            elif len(nums) == 3:
                i = 0

            integer += (nums[0] * 100 + i) * 1000

        else:
            if len(nums) == 2:
                integer += nums[0] * 1000

    return integer
