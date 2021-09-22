def duplicate_count(text):
    text = text.lower()
    return len(list(filter(lambda n: n > 1, [text.count(char) for char in set(text)])))
