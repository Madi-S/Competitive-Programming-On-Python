def amount_of_pages(summary):
    # 1-9:          9       = 9 * 1 * 10**0
    # 10-99:        180     = 9 * 2 * 10**1
    # 100-999:      2700    = 9 * 3 * 10**2
    # 1000-9999:    36000   = 9 * 4 * 10**3
    # 10000-99999:  450000  = 9 * 5 * 10**4
    res = 0
    for x in range(1, 6):
        y = 9 * x * 10**(x-1)
        if summary <= y:
            return res + summary//x
        res += y//x
        summary -= y
