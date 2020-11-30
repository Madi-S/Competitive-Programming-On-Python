'''
From https://acmp.ru/index.asp?main=task&id_task=922
'''


def count_time(t1, t2, s1, s2, s):
    if s2 >= s1:
        return 'NO'
    time_count = 0
    distance_traveled = 0
    while distance_traveled < s:
        left = s - distance_traveled
        if left <= s1:
            distance_traveled += left
            time_count += t1
            break

        distance_traveled += s1
        time_count += t1

        distance_traveled -= 1
        time_count += t2

    return time_count


print(count_time(10, 1, 100, 20, 500))
