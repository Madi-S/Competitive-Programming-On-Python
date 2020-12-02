
with open('INPUT.TXT') as rf:
    m = [int(e) for e in rf.read().split('\n')[1].split(' ')]
    with open('OUTPUT.TXT', 'w') as wf:
        wf.write(str(min(m))+' '+str(max(m)))
