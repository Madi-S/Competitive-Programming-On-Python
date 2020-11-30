'''
From https://acmp.ru/index.asp?main=task&id_task=922
'''


def count_time(t1, t2, s1, s2, s):
    if s2 >= s1:
        return 'NO'
    time_count = distance_traveled = 0
    while distance_traveled < s:
        print(time_count, distance_traveled)
        left = s - distance_traveled
        if left <= s1:
            print('here', left)
            distance_traveled += left
            time_count += (left / s1) * t1
            break

        distance_traveled += s1
        time_count += t1

        distance_traveled -= s2
        time_count += t2

    return round(time_count, 2)


print(count_time(10, 1, 100, 20, 500))
