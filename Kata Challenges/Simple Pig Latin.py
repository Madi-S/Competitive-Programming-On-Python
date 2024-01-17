from string import punctuation


def pig_it(text):
    print(text)
    res = []
    words = text.split(' ')
    for word in words:

        # Check against empty strings '' and singular punctuation strings '?' or ','
        if word and not word in punctuation:

            # Handle punctuation:
            # 1) Create temporary variables, which store punctuation on left and on right
            # 2) In the end add combine modified word with stored punctuation
            add_left = ''
            add_right = ''

            if word[0] in punctuation:
                add_left = word[0]
                word = word[1:]

            elif word[-1] in punctuation:
                add_right = word[-1]
                word = word[:-1]

            # 1) Move first letter to the end
            # 2) Add 'ay' to the end

            first_letter = word[0]
            word = word[1:] + first_letter + 'ay'

            word = add_left + word + add_right
        res.append(word)

    return ' '.join(res)


print(pig_it('Quis custodiet ipsos custodes ?'))
