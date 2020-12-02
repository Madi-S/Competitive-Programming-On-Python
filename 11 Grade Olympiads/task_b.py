

with open('INPUT.TXT') as rf:
    with open('OUTPUT.TXT','w') as wf:
        wf.write(str(max([len(e) for e in rf.read().split('1')])))
