

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0

        while len(left) and len(right):
            if left[0] <= right[0]:
                array[i] = left.pop(0)

            else:
                array[i] = right.pop(0)

            i += 1

        while len(left):
            array[i] = left.pop(0)
            i += 1

        while len(right):
            array[i] = right.pop(0)
            i += 1

    return array


print(merge_sort([3, 65, 43, 98, 65, 32]))
