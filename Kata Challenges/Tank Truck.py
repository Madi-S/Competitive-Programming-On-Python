import math


def tankvol(h, d, vt):
    '''
    Calculates the remaining volume of the liquid in a tank truck
    h - height of remaining liquid
    d - diameter of cylinder
    vt - total volume of tank truck
    '''

    '''
    Firstly, find alpha / 2 (cos of (R - h) and R )
    Secondly, calculate the area A of circular segment    
        remaining liquid in 2D
    Thirdly, find l (length of cylinder)
        l = Volume / (Pi * R ** 2) 
    Finally, return a multiplication of l and A
    '''
    radius = d / 2
    total_volume = vt
    height = radius - h

    halved_alpha = math.acos(height / radius)
    alpha = math.degrees(halved_alpha * 2)

    area = (radius ** 2) * (math.pi * alpha /
                            180 - math.sin(math.radians(alpha))) / 2


    length = total_volume / (math.pi * radius ** 2)

    result = abs(math.floor(area * length))

    return result


print(tankvol(40, 120, 3500))
