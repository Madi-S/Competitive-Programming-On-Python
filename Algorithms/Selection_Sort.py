# Selection sort pushes minimum element to the end
# Thus this sort method divides array in two: first part with minimum elements - sorted, second - unsorted

from random import randint


def sort(arr):
    for i in range(len(arr) - 1):
        # Store minimum position - it will increase over time because left part will become sorted and no need to check these values because they are the min values
        min_pos = i

        # Loop through the array and find the min value
        for j in range(i, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j

        # Swap min value with value found at min position
        arr[i], arr[min_pos] = arr[min_pos], arr[i]

        print(f'Processing:   {arr}')
        
    return arr


arr = [randint(1, 1000) for _ in range(10)]
print(f'Given array:  {arr}')
print(f'Sorted array: {sort(arr)}')
