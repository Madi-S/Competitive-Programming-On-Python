
def purify_word(word):
	word = word.lower().replace('/','').replace('.','').replace(',','')
	print(word)
	if 'l' in word or 'n' in word:
		return word 
	else:
		return word.replace('"','').replace("'",'')


def top_3_words(text):
	words = text.replace('-','').split(' ')
	top = {}
	
	for word in words:
		word = purify_word(word.lower())
		if word:
			if not word in top:
				top[word] = 1
			else:
				top[word] += 1

	top = dict(sorted(top.items(), key=lambda counter: counter[1], reverse=True))
	return list(top.keys())[:3]

print(top_3_words("  '''  ")) 

['xgvdtvrffqk-:?qsicogdy!;ffqk', ':', "ff'qk_xgvdtvr-;txhndyslar-_;iuyyndonz-iuyyndonz"]. 
One possible valid answer: ['xgvdtvr', "ff'qk", 'txhndyslar']