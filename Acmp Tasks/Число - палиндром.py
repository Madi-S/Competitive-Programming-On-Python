'''
From https://acmp.ru/index.asp?main=task&id_task=173

Напомним, что палиндромом называется строка, одинаково читающаяся с обеих сторон. Например, строка «ABBA» является палиндромом, а строка «ABC» - нет.
Необходимо определить, в каких системах счисления с основанием от 2 до 36 представление заданного числа N является палиндромом.
В системах счисления с основанием большим 10 в качестве цифр используются буквы английского алфавита: A, B, ... , Z. Например, A11 = 1010, Z36 = 3510.
'''


from sys import setrecursionlimit


def find(a):
    def convert_base(num, to_base, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        # now convert decimal to 'to_base' base
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if n < to_base:
            return alphabet[n]
        else:
            return convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def check_reversed(num: str):
        for n in range(len(num) // 2):
            if num[n] != num[-n-1]:
                return False

        return True

    variations = []
    for i in range(2, 37):
        print(i)
        converted = convert_base(a, i)
        if check_reversed(str(converted)):
            variations.append(i)

    if len(variations) > 1:
        print('Multiple')
        print(variations)

    elif len(variations):
        print('Unique')
        print(variations)

    else:
        print(None)


find(123)
