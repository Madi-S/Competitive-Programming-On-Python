from functools import reduce
from itertools import cycle

def reduce_by_rules(lst, rules):
 	r = cycle(rules)
 	return reduce(lambda a, b: next(r)(a, b), lst)



rules = [lambda a, b: a + b, lambda a, b: a - b]
print(reduce_by_rules([2.0, 2.0, 3.0, 4.0], rules))