''' Zodiac: (
        (Month number, (From day, To day))
        (Month number, (From day, To day))
    )
'''
zodiac_signs_by_days = {
    'Aquarius': (
        (1, (21, 31)),
        (2, (1, 19))
    ),
    'Pisces': (
        (2, (20, 31)),
        (3, (1, 20))
    ),
    'Aries': (
        (3, (20, 31)),
        (4, (1, 20))
    ),
    'Taurus': (
        (4, (20, 31)),
        (5, (1, 21))
    ),
    'Gemini': (
        (5, (22, 31)),
        (6, (1, 21))
    ),
    'Cancer': (
        (6, (22, 31)),
        (7, (1, 22))
    ),
    'Leo': (
        (7, (23, 31)),
        (8, (1, 23))
    ),
    'Virgo': (
        (8, (24, 31)),
        (9, (1, 23))
    ),
    'Libra': (
        (9, (24, 31)),
        (10, (1, 23))
    ),
    'Scorpio': (
        (10, (23, 31)),
        (11, (1, 22))
    ),
    'Sagittarius': (
        (11, (23, 31)),
        (12, (1, 21))
    ),
    'Capricorn': (
        (12, (22, 31)),
        (1, (1, 20))
    )
}


def star_sign(date):
    date = date.__str__()
    _, month, day = date.split('-')
    day = int(day)
    month = int(month)
    for zodiac, _range in zodiac_signs_by_days.items():
        for _month, days_range in _range:
            if month == _month:
                if day >= days_range[0] and day <= days_range[1]:
                    return zodiac
