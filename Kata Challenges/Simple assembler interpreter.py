def simple_assembler(program):
    register = {}
    commands = program.split('\n')

    prev_command = None

    for command in commands:
        command = command.split()
        instruction = command[0]

        if instruction == 'mov':
            x, y = command[1:]

            # x and y are letters
            if y in register.keys():
                register[x] = register[y]

            # x is str and y is integer
            else:
                register[x] = int(y)

        if instruction == 'inc':
            x = command[1]
            register[x] = register[x] + 1

        if instruction == 'dec':
            x = command[1]
            register[x] = register[x] - 1

        if instruction == 'jnz':
            x, y = command[1:]

            prev_instruction = prev_command[0]
            while register[x] != 0:
                if prev_instruction == 'dec':
                    prev_x = prev_command[1]

                elif prev_instruction == 'inc':
                    prev_x = prev_command[1]

                else:
                    break

        prev_command = command

    return {}
