from functools import cmp_to_key


def sort_by_weight(w1, w2):
    sum1 = sum(list(map(int, w1)))
    sum2 = sum(list(map(int, w2)))
    if sum1 < sum2:
        return -1
    elif sum1 > sum2:
        return 1

    min_ = min(w1, w2)
    if min_ == w1:
        return -1
    elif min_ == w2:
        return 1

    return 0


def order_weight(string):
    normal_order = string.split(' ')
    return ' '.join(sorted(normal_order, key=cmp_to_key(sort_by_weight)))


print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))
# 11 11 2000 10003 22 123 1234000 44444444 9999
# 11 11 2000 10003 22 123 1234000 44444444 9999
