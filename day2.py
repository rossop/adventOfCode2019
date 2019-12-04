with open('day2_input.txt') as f:
    instructionsList = f.read()

instructionsList = instructionsList.rstrip('\n').split(',')
instructionsList = [int(i) for i in instructionsList]



def Intcode (instructionsList, noun = 12, verb = 2):

    """ Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode,
    if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3,
    and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters

    """
    it  = 0


    instructionsList[1] = noun
    instructionsList[2] = verb



    while True:
        instruction = instructionsList[it:it+4]
        if instruction[0] == 1:
            instructionsList[instruction[3]] = instructionsList[instruction[1]] \
                                     + instructionsList[instruction[2]]

        elif instruction[0] == 2:
            instructionsList[instruction[3]] = instructionsList[instruction[1]] \
                                     * instructionsList[instruction[2]]

        elif instruction[0] == 99:
            break
        it += 4
        if it > len(instructionsList):
            break

    return instructionsList



instructions = Intcode(instructionsList)
print('Day2:\n{}\n'.format(str(instructions[0])))
print(len())


for ii in range(100):
    for jj in range(100):
        instructions = Intcode(instructionsList, ii, jj)
        if instrunctions[0] == 19690720:
            print(str(ii)+str(jj))
            break



