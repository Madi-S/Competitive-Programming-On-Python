'''
A famous casino is suddenly faced with a sharp decline of their revenues. 
They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?

The characteristics of the string of cards are:

Each card consists of two characters, where
The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
A space is used as card separator between cards
'''

ranking = {'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

'''
High-Card: 2-14
One-Pair: 14 + pair's rank / 10 (14.2-15.4)
Two-Pair: 15.4 + pair's rank / 10  (15.4-16.8)
Tree of a Kind: 16.8 + three's rank / 10 (16.8-18.2)
Straight: 18.2 + highest card / 10 (18.2-19.6)
Flush: 19.6 + highest card / 10 (19.6-21)
Full House: 21 + three's rank + highest card of 2 / 10 (21-36.4)
Four of a Kind: 36.4 + four's rank + fifth card / 10
Straight Flush: 60 + highest card + 2nd highest / 10 + 3rd highest / 100 ...
Royal Flush: 100 + hihghest card + 2nd highest / 10 + ... 
'''

class PokerHand(object):

	def __init__(self, hand):
		self.hand = hand.split(' ')
		self.set_values()
		self.set_suit()
		self.derive_pattern()
		self.derive_rank()

	def set_suit(self):
		self.suit = [e[-1] for e in self.hand]


	def set_values(self):
		self.values = [ranking[e[:-1]] for e in self.hand]
		self.values.sort()


	def isFlush(self):
   		return True if self.suit.count(self.suit[0]) == 5 else False


	def isStraight(self):
		for i, v in enumerate(self.values[:-1]):
			if v != self.values[i+1] - 1:
				break
		else:
			return True
		return False


	def get_counts(self):
		counts = {}
		for v in self.values[::-1]:
			count = self.values.count(v)
			if count == 2:
				counts[v] = count
			elif count == 3:
				counts[v] = count
			elif count == 4:
				counts[v] = count
				break
		return counts


	def derive_pattern(self):
		self.flush = self.isFlush()
		self.straight = self.isStraight()
		self.counts = self.get_counts()
		self.highest = self.values[-1]


	def derive_rank(self):
		self.rank = 0

		if self.straight:
			self.rank += 400

		if self.flush:
			self.rank += 500

		elif len(self.counts) == 1 and 2 in self.counts.values():
			self.rank += 100

		elif len(self.counts) == 2 and not 3 in self.counts.values():
			self.rank += 200

		elif len(self.counts) == 1 and 3 in self.counts.values():
			self.rank += 300 

		elif 3 in self.counts.values() and len(self.counts) == 2:
			self.rank += 600 

		elif 4 in self.counts.values():
			self.rank += 700

		for i, v in enumerate(self.values[::-1]):
			self.rank += v * 10 ** -i
		print(self.rank)


	def compare_with(self, other):
		if self.rank == other.rank:
			return 'Tie'
		elif self.rank < other.rank:
			return 'Loss'
		else:
			return 'Win'


p = PokerHand("JS JD JC JH AD")
print(p.compare_with(PokerHand("2S AH 2H AS AC")))