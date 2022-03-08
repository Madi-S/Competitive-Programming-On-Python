rules = {
    # hunter: (*preys)
    'antelope': ('grass',),
    'big-fish': ('little-fish', ),
    'bug': ('leaves',),
    'bear': ('big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'),
    'chicken': ('bug',),
    'cow': ('grass',),
    'fox': ('chicken', 'sheep'),
    'giraffe': ('leaves',),
    'lion': ('antelope', 'cow'),
    'panda': ('leaves', ),
    'sheep': ('grass',)
}


'''
Notes:

- Animals can only eat things beside them

- Animals always eat to their LEFT before eating to their RIGHT

- Always the LEFTMOST animal capable of eating will eat before any others

- Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible
'''


def who_eats_who(zoo):
    initial_zoo = zoo
    zoo = zoo.split(',')
    result = []

    while True:
        dead_animals = []
        for i, animal in enumerate(zoo):
            # Skip if animal does not eat anything
            if not animal in rules.keys():
                continue

            # SKip if animal is already eaten by something
            if i in dead_animals:
                continue

            # Try eating left
            if i != 0:
                left_prey = zoo[i - 1]
                if left_prey in rules[animal]:
                    result.append(f'{animal} eats {zoo[i - 1]}')
                    dead_animals.append(i - 1)
                    # Break because leftmost animal should try eating again
                    break

            # Try eating right
            if i != len(zoo) - 1:
                right_prey = zoo[i + 1]
                if right_prey in rules[animal]:
                    result.append(f'{animal} eats {zoo[i + 1]}')
                    dead_animals.append(i + 1)
                    # Break because leftmost animal should try eating again
                    break

        if not dead_animals:
            break

        dead_animals.sort(reverse=True)

        for dead_animal in dead_animals:
            zoo.pop(dead_animal)

    return [initial_zoo, *result, ','.join(zoo)]


print(who_eats_who("fox,bug,chicken,grass,sheep"))
