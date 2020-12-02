'''
From https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=25&id_topic=64&id_problem=357
'''

import re


def count(x, y, s):
    pattern = re.compile(r'[\w]+')
    rows = [[e] for e in s.split('\n')]
    ships = []
    for i in range(len(rows)):
        # If we find something like X or S in the row
        matches = pattern.finditer(''.join(rows[i]))
        if matches:
            for match in matches:
                # Init ship variable to store letters
                ship = str()

                # Mark our start, end parameters - so we can dig down only these coordinates
                another_range = [match.span()]

                # Append ship letters
                ship += match.group()
                print(f'Initial ship is: {ship}')

                # Mark our findings as `-` so we will not encouter it multiple times
                rows[i][match.start(): match.end()] = '-' * len(match.group())
                print(f'Row #{i} changed now to: {rows[i]}')

                # Start to dig down (look for other parts of the ship below, starting from row below)
                # Check if we are not digging down from the last row
                if i + 1 < len(rows):
                    for another_row in rows[i+1:]:
                        print(
                            f'Digging down {another_row} with the match {match}')
                        # Create a string, which we are going to search for X and S inside
                        to_dig = ''

                        # Row level/index we are currently working with
                        index = rows.index(another_row)

                        print(f'Before clearing: {rows[index]}')
                        for pos in another_range:
                            to_dig += ''.join(another_row[pos[0]: pos[1]])

                            # Change digged values from 'S' or 'X' to '-', so we will not encounter them a second time
                            for k in range(pos[0], pos[1]):
                                try:
                                    print(
                                        f'{rows[index][k]} is gonna change to `-`')
                                    rows[index][k] = '-'
                                except:
                                    print('exception found')

                        print(f'After clearing: {rows[index]}')
                        # Clear coordinates/positions, which we already worked with -> start digging based on new positions, retrieved form matching them
                        another_range.clear()

                        # Search for X and S in our special string for next digging
                        another_matches = pattern.finditer(to_dig)
                        print(
                            f'Another matches {[match.group() for match in another_matches]} that were found in to_dig {to_dig}')
                        if another_matches:
                            for another_match in another_matches:
                                another_range.append(another_match.span())
                        else:
                            break
                        print(f'Next time gonna dig down for: {another_range}')
                # Append ship to the ships with its status (demolished, untouched, damaged)
                if 'S' in ship and 'X' in ship:
                    ships.append({ship: 'damaged'})
                elif 'S' in ship:
                    ships.append({ship: 'untouched'})
                else:
                    ships.append({ship: 'demolished'})

    print(ships)


count(3, 8, '''XX-SSS--
X---S-X-
X-S---S-''')

'''
XX-SSS--
X---S-X-
X-S---S-
'''
