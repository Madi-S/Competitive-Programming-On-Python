'''
From https://acmp.ru/index.asp?main=task&id_task=952

Цена проезда в автобусах нашего города — один рубль.
Однако, не все так просто — каждый взрослый пассажир имеет право провезти бесплатно не более одного ребенка. 
Это значит, что взрослый пассажир, который провозит с собой k (k > 0) детей, платит всего k рублей:
за один билет для себя и за (k - 1) билетов для своих детей.
Также взрослый может ехать без детей, в этом случае он платит всего один рубль.
Известно, что дети не могут проезжать в автобусе без сопровождения взрослых.
Помогите посчитать минимальную и максимальную стоимость проезда в рублях, которую могли заплатить пассажиры автобуса.
'''


def count_prices(adults: int, childs: int):
    if adults and childs:
        return childs, adults + childs - 1

    elif adults and not childs:
        return adults, adults

    return 'Impossible'


print(count_prices(5, 5))
