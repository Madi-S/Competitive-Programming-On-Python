def move_zeros(array):
    zeros_count = 0
    while 0 in array:
        array.remove(0)
        zeros_count += 1
    array.extend([0 for _ in range(zeros_count)])
    return array
