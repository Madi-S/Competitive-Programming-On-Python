'''

The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language; Shell bash, PowerShell and Fortran return a string) with the size of each of the squares.

'''


def sqInRect(x, y):
    if x == y:
        return None

    result = []
    while y != x:
        if y > x:
            y -= x
            result.append(x)
        elif x > y:
            x -= y
            result.append(y)

    result.append(y)

    return result
