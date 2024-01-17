def anagrams(word, words):
    word = sorted(word)
    res = [w for w in words if sorted(w) == word]
    return res


print(anagrams('abba', ['bbaa', 'abba', 'bbba', 'abab']))
