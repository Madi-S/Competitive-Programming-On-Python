from random import randint  # To create pseudorandom array to sort


def merge_sort(arr):
    # If left or right array has more than 1 element
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Left part of the array (from start to the middle), middle not included
        L = arr[:mid]

        # Right part of the array (from middle to the end), middle included
        R = arr[mid:]

        # Calling function itself but passing the left part of the array
        merge_sort(L)

        # Calling function itself but passing the right part of the array
        merge_sort(R)

        # Defining indexes (arrows), i - index for sorted array
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while k < len(L) and j < len(R):
            # If value from the left array is less than value from the right array -> insert this value at `i` position in `arr`
            if L[k] < R[j]:
                arr[i] = L[k]
                k += 1
            # Else do the same but with value from the right array
            else:
                arr[i] = R[j]
                j += 1
            # Increment index value after one insertion
            i += 1

        # Check if any element left in the left array
        while k < len(L):
            arr[i] = L[k]
            i += 1
            k += 1

        # Check if any element left in the right array
        while j < len(R):
            arr[i] = R[j]
            j += 1
            i += 1

    return arr


# Driver Code
arr = [randint(1, 100) for _ in range(10)]
print(f'Given array is:  {arr}')
sorted_arr = merge_sort(arr)
print(f'Sorted array is: {sorted_arr}')
