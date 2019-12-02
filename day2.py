with open('day2_input.txt') as f:
    instructionsList = f.read()

instructionsList = instructionsList.rstrip('\n').split(',')
instructionsList = [int(i) for i in instructionsList]



def Intcode (instructionsList):

    """ Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode,
    if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3,
    and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters

    """
    it  = 0

    noun = 12
    verb = 2
    instructionsList[1] = 12
    instructionsList[2] = 2

    predictionList = []

    while True:
        instruction = instructionsList[it:it+4]
        if instruction[0] == 1:
            instructionsList[instruction[3]] = instructionsList[instruction[1]] \
                                     + instructionsList[instruction[2]]
            predictionList += [1,0,0,0]

        elif instruction[0] == 2:
            instructionsList[instruction[3]] = instructionsList[instruction[1]] \
                                     * instructionsList[instruction[2]]
            predictionList += [2,0,0,0]
        elif instruction[0] == 99:
            predictionList += [99]
            break
        it += 4
        if it > len(instructionsList):
            break

    return instructionsList, predictionList

instructions, predictions = Intcode(instructionsList)
print('Day2:\n{}\n{}'.format(str(instructions),str(predictions)))