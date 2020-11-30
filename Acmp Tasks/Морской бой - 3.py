'''
From https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=25&id_topic=64&id_problem=357
'''

import re


def count(n, m, battle):
    hor = [list(i) for i in battle.split('\n')]
    shipss = []
    print(hor[0], '\n', hor[1], '\n', hor[2])
    for p in range(len(hor)):
        res = re.finditer(r'[\w]+', ''.join(hor[p]))
        for r in res:
            ships = []
            print(f'R of res {r.group()} appended')
            ships.append(r.group())
            i = p + 1
            while i < len(hor):
                st, end = r.start() + 1, r.end() + 1
                to_search = ''.join(hor[i][st:end])
                res2 = re.match(r'[\w]+', st, end)
                print(f'{res2} in {to_search}')
                for j in range(st, end):
                    hor[i][j] = '-'
                if res2:
                    print(f'Res2 {res2.group()} appended')
                    ships.append(res2.group())
                else:
                    break
                i += 1
            shipss.append(ships)
    print(shipss)


count(3, 8, '''X--SSS--
XX--S-X-
X-S---S-''')
