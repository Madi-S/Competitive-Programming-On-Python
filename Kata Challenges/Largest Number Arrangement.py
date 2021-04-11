def largest_arrangement(numbers):
    res = ''
    digits = {}
    
    for num in numbers:
        digit = str(num)[0]
        if digit in digits:
            digits[digit].append(num)
        else:
            digits[digit] = [num, ]

    for digit in sorted(list(digits.keys()), reverse=True):
        nums_len = [[num, len(str(num))] for num in digits[digit]]
        max_len = len(str(max(digits[digit])))
        
        for i, num_len in enumerate(nums_len):
            filled_num = str(num_len[0])
            while len(filled_num) < max_len:
                filled_num += filled_num
                
            nums_len[i][0] = filled_num
            
        for num, length in sorted(nums_len, reverse=True):
            res += str(num)[:length]
            
            
    return int(res)
    