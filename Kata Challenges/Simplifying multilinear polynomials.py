def simplify(poly):
    poly += '+'
    if not poly[0] in '+-':
        poly = '+' + poly
    
    compounds = []
    compound = ''

    for char in poly:
        if char in '+-':
            if compound:
                compound = ''.join(sorted(compound))
                if compound[0].isdigit():
                    digit = compound[0]
                    compound = compound[1:]
                else:
                    digit = '1'

                compounds.append((sign, digit, compound))
                compound = ''
            
            sign = char
        
        else:
            compound += char

    groups = {}
    compounds = sorted(compounds)

    for compound in compounds:
        variable = compound[-1]

        if variable in groups.keys():
            groups[variable].append(int(''.join(compound[:-1])))
        else:
            groups[variable] = [int(''.join(compound[:-1])),]

    variables_to_delete = []

    for key, values in groups.items():
        sum_ = sum(values)

        if sum_ == 0:
            variables_to_delete.append(key)
        elif sum_ == 1:
            sum_ = '+'
        elif sum_ == -1:
            sum_ = '-'
        elif sum_ > 0:
            sum_ = '+' + str(sum_)
        else:
            sum_ = str(sum_)

        groups[key] = sum_
        
    for variable_to_delete in variables_to_delete:
        del groups[variable_to_delete]

    var_length = {(variable, number): len(variable) for variable, number in groups.items()}
    length_var = {}

    for tupl, length in var_length.items():
        if length in length_var.keys():
            length_var[length].append(tupl)
        else:
            length_var[length] = [tupl,]

    simplified = ''

    for length, values in sorted(length_var.items()):

        for tupl in sorted(values):
            val = tupl[-1] + tupl[0]
            simplified += val

    if simplified.startswith('+'):
        simplified = simplified[1:]
    
    return simplified

print(simplify('a+ac-ab')) 

print('\na+ac-ab should equal a-ab+ac')