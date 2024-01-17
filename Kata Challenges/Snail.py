def snail(snail_map):
    res = []
    while len(snail_map) > 0:
        res += snail_map.pop(0)  # Delete first element and assign it

        # Check if snaile map has elements
        if len(snail_map) > 0:
            for i in snail_map:

                # Loop through the sub-arrays, and append last number from each sub-array to result, starting from last sub-array
                res += [i.pop()]

            # If snail map is not empty
            if snail_map:
                # Append and delete last reversed sub-array
                res += snail_map.pop()[::-1]

            # Loop through reversed snail map
            for i in snail_map[::-1]:
                # Append and delete first number from sub-array
                res += [i.pop(0)]

    return res
