def filter_list(l):
    return list(filter(lambda a: isinstance(a, int), l))


print(filter_list([1, 2, 'a', 'b']))
