num = input()

# Если строка палиндром, то возвращаем её саму
if num == num[::-1]:
    print(num)

# Если число цифр чётное
if len(num) % 2 == 0:
    # Выделяем левую часть, чтобы зафиксировать левое отражение палиндрома
    left_part = num[:len(num) // 2]

    # Если левая часть + перевёрнутая левая часть меньше итогового числа
    if int(left_part + left_part[::-1]) < int(num):
        # Увеличиваем левую часть на единицу
        left_part = str(int(left_part) + 1)

    # Возвращаем левую часть + перевёрнутую левую часть
    print(int(left_part + left_part[::-1]))

# Если число цифр чётное
else:
    # Выделяем центральная цифра палиндрома
    mid_digit = num[len(num) // 2]
    # Выделяем левую часть
    left_part = num[:len(num) // 2]

    # Если левая часть + центральная цифра + перевёрнутая левая часть
    # меньше итогового числа
    if int(left_part + mid_digit + left_part[::-1]) < int(num):
        # Склеиваем левую часть и центральную цифру, переводим в формат
        # числа и увеличиваем на единицу
        left_part_with_mid = str(int(left_part + mid_digit) + 1)

        # Разъединяем левую часть и центральную цифру
        ledt_part = left_part_with_mid[:-1]
        mid_digit = left_part_with_mid[-1]

    # Возвращаем левую часть + центральную цифру + перевёрнутую
    # левую часть
    print(left_part + mid_digit + left_part[::-1])