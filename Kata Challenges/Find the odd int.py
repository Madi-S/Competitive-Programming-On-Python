def find_it(seq):
    vals = set(seq)
    for val in vals:
        c = seq.count(val)
        if c % 2 != 0:
            return val
