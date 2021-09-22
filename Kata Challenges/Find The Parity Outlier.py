def find_outlier(integers):
    # Determine whether array contains even or odd integers by checking first three integers
    odd_ints = []
    even_ints = []

    for integer in integers[:3]:
        if integer % 2 == 0:
            even_ints.append(integer)
        else:
            odd_ints.append(integer)

    # Define is_outlier function based on odd or even integers array, if there is any in the opposite array -> return it
    if len(even_ints) > len(odd_ints):
        def is_outlier(a): return a % 2 != 0
        if odd_ints:
            return odd_ints.pop()
    else:
        def is_outlier(a): return a % 2 == 0
        if even_ints:
            return even_ints.pop()

    # Check for outlier
    for integer in integers:
        if is_outlier(integer):
            return integer
