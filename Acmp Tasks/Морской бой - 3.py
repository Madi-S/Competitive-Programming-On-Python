'''
From https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=25&id_topic=64&id_problem=357
'''

import re


def count(n, m, battle):
    hor = [i for i in battle.split('\n')]
    print(hor[0], '\n', hor[1], '\n', hor[2])
    for p in hor:
        res = re.finditer('[\w]+', p)
        for r in res:
            print(r.group(), r.span(), p)


count(3, 8, '''---SSS--
XX--S-X-
X-S---S-''')
