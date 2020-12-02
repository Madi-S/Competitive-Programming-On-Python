

with open('INPUT.TXT') as rf:
    temp = {int(e.replace(' ', '')): e for e in rf.read()
            [1:].strip().split('\n')}
    sorted_ = list(temp.keys())
    sorted_.sort()
    with open('OUTPUT.TXT', 'w') as wf:
        for time in sorted_:
            wf.write(temp[time]+'\n')
