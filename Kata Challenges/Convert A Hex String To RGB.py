def hex_string_to_RGB(hex_string):
    r, g, b = hex_string[1:3], hex_string[3:5], hex_string[5:7]
    return {
        'r': int(r, 16),
        'g': int(g, 16),
        'b': int(b, 16)
    }
