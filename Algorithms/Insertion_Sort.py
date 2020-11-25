# Divide unsorted array into two parts:
# First part intitally consist of the left most element, thus the seconds is all elements excluding the first one
# After splitting our sequence, we take one by one every element from the seconds part and compare them
# Hence, we keep pushing element untill it hits the end of the list or the next left value will be less than pushed value -> keep its position


def sort(a):
    # Start from the second value already
    for i in range(1, len(a)):
        # Swap values until left value is less equal than the a[i] (value we are currently working with) and i is positive number
        while a[i-1] > a[i] and i > 0:
            a[i-1], a[i] = a[i], a[i-1] # Swap left value with current
            i -= 1                      # Decrease counter i by 1 (because then we will work with value left by 1)

    return a


print(sort([434243, 23, 2132, 2342, 34234234, 23, 423, 42, 34, 234]))
