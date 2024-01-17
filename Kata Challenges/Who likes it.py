def likes(names):
    if not names:
        return 'no one likes this'
    res = [names.pop(0)]

    if names:

        if len(names) >= 3:
            othres_count = len(names) - 1
            names = names[:1]

            names.append(str(othres_count) + ' others')

        for name in names:
            res.append(', ' + name)

        res[-1] = ' and' + res[-1][1:]
        res += ' like'

    else:
        res += ' likes'
    res += ' this'

    return ''.join(res)


'''
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
'''
print(likes(["Alex", "Jacob", "Mark", "Max", "Max"]))
