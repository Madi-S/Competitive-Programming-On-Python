def spin_words(sentence):
    return ' '.join(list(map(lambda a: a[::-1] if len(a) >= 5 else a, sentence.split())))


spin_words("Hey fellow warriors")
spin_words("This is a test")
spin_words("This is another test")
