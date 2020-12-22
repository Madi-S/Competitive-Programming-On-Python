

class User:

	_ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

	def __init__(self):
		self._rank = self._ranks[0]
		self._progress = 0

	@property
	def progress(self):
		return self._progress

	@property
	def rank(self):
		# if self._rank == 0:
		# 	self._rank = 1
		# elif self._rank > 8:
		# 	self._rank = 8
		return self._rank

	def inc_progress(self, activity_rank: int):
		diff = self._ranks.index(activity_rank) - self._ranks.index(self._rank)
		if diff <= -2:
			return
		elif diff == 0:
			diff = 1 
		