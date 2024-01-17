def page_digits(pages):
    res = 0
    i = 1
    while True:
        print(res, i)
        n_pages = 9 * 10 ** (i - 1)
        # 10 - 1 = 9
        # 100 - 10 = 90
        # 1000 - 100 = 900

        if pages <= n_pages:
            res += pages * i
            # 3 * 1 = 3
            # 70 * 2 = 140
            # 400 * 3 = 1200
            break
        else:
            res += n_pages * i
            pages -= n_pages
            # 9 * 1 = 9
            # 90 * 2 = 180
            # 900 * 3 = 2700
        i += 1
    return res


print(page_digits(100))
