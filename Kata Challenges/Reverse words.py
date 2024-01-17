def reverse_words(text):
    result = ''
    word = ''
    for i, ch in enumerate(text):
        if ch == ' ':
            result += word[::-1] + ' '
            word = ''
        else:
            word += ch
    result += word[::-1]
    return result
