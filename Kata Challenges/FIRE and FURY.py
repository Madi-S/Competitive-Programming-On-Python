def fire_and_fury(tweet):
    if not tweet.count('FIRE') and not tweet.count('FURY'):
        return 'Fake tweet.'

    unique_letters = set(tweet)
    working_letters = 'EFIRUY'

    while unique_letters:
        if not unique_letters.pop() in working_letters:
            return 'Fake tweet.'

    i = 0
    res = ''
    fire_count = 0
    fury_count = 0
    length = len(tweet)

    while i + 4 <= length:
        word = tweet[i: i + 4]
        if word == 'FIRE':
            fire_count += 1
            i += 4
            if fury_count:
                res += ' I am {}furious.'.format('really ' * (fury_count - 1))
                fury_count = 0

        elif word == 'FURY':
            fury_count += 1
            i += 4
            if fire_count:
                res += ' You {}are fired!'.format(
                    'and you ' * (fire_count - 1))
                fire_count = 0

        else:
            i += 1

    if fire_count:
        res += ' You {}are fired!'.format('and you ' * (fire_count - 1))
    if fury_count:
        res += ' I am {}furious.'.format('really ' * (fury_count - 1))

    return res[1:]
