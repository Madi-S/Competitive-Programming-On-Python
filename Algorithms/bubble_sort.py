# Bubble sort: is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.


def bubble_sort(array, desc=False):
    if not desc:
        compare = lambda a,b: a > b
    else:
        compare = lambda a,b: a < b
    
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if compare(array[j], array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

    return array

print(bubble_sort([3, 54, 1, 0, 24]))       # [0, 1, 3, 24, 54] Ascending order
print(bubble_sort([3, 54, 1, 0, 24], True)) # [54, 24, 3, 1, 0] Descending order
