'''
From https://acmp.ru/index.asp?main=task&id_task=905
'''


def solve(txt):
    import re
    key = 'the quick brown fox jumps over the lazy dog'.replace(' ', '')
    match = re.search(
        r'[\w]{3} [\w]{5} [\w]{5} [\w]{3} [\w]{5} [\w]{4} [\w]{3} [\w]{4} [\w]{3}', txt.strip())

    if not match or len(set(i for i in match.group())) != 27:
        return 'No solution'
    else:
        secret = match.group().replace(' ', '')
        cipher = {secret[i]: key[i] for i in range(len(key))}
        cipher.update({'\t': '\t', '\n': '\n', ' ': ' '})
    return ''.join([cipher[l] for l in txt])


print(solve('''vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
xnm fffff lrtzv iia wwwfd tsmr xnm ypwq ktj
frtjrpgguvj otvxmdxd prm iev prmvx xnmq'''))
