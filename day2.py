# with open('day2_input.txt') as f:
#     instructionsList = f.read()
#
# instructionsList = instructionsList.rstrip('\n').split(',')
# instructionsList = [int(i) for i in instructionsList]


def run_program(insList, noun=12, verb=2):
    """ Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode,
    if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3,
    and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters

    :05/12/2019: Updated using loociano (https://github.com/loociano) solution
    :return: processed list
    """
    insList[1] = noun
    insList[2] = verb
    it = 0
    while it < len(insList):
        opcode = insList[it]
        op1 = insList[insList[it + 1]]
        op2 = insList[insList[it + 2]]
        dest = insList[it + 3]
        if opcode == 99:
            break
        else:
            if opcode == 1:
                insList[dest] = op1 + op2

            elif opcode == 2:
                insList[dest] = op1 * op2

            else:
                print('ERROR: undefined opcode')
                break
            it += 4

    return insList


def run_day2():
    """
    Finds solutions for second day problem
    :return: results for each part of the question
    """
    with open('day2_input.txt') as f:
        insList = list(map(int, f.read().rstrip('\n').split(",")))
    instructions = intcode(insList)
    print('Day2:\n{}'.format(str(instructions[0])))

    for noun in range(100):
        for verb in range(100):
            try:
                # TODO why do i have to import here?
                with open('day2_input.txt') as f:
                    insList = list(map(int, f.read().rstrip('\n').split(",")))
                instructions = intcode(insList, noun, verb)
                if instructions[0] == 19690720:
                    print(str(noun) + str(verb))
                    code = noun * 100 + verb
                    break
            except:
                continue

    return instructions[0], code


part1, part2 = run_day2()
