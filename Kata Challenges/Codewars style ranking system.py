

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
        return self._rank

    def inc_progress(self, activity_rank: int):
        print(self._rank, self._progress, activity_rank)
        diff = self._ranks.index(activity_rank) - self._ranks.index(self._rank)

        if diff <= -2:
            return
        elif diff == 0:
            diff = 1

        self._progress += diff ** 2 * 10
        while self._progress >= 100 and self._rank < 9:
            self._rank += 1
            self._progress -= 100
        print(self._rank, self._progress, activity_rank)
