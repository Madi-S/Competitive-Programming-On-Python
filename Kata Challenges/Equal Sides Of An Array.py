def find_even_index(arr):
    l_sum = 0
    r_sum = sum(arr[1:])
    for i in range(len(arr)):
        if r_sum == l_sum:
            return i
        l_sum += arr[i]
        if i + 1 == len(arr):
            r_sum = 0
        else:
            r_sum -= arr[i + 1]
    return -1


print(find_even_index([1, 2, 3, 4, 5, 6]))
