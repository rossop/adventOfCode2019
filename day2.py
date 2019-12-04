# with open('day2_input.txt') as f:
#     instructionsList = f.read()
#
# instructionsList = instructionsList.rstrip('\n').split(',')
# instructionsList = [int(i) for i in instructionsList]

with open('day2_input.txt') as f:
    insList = list(map(int, f.read().rstrip('\n').split(",")))

def intcode (instructionsList, noun = 12, verb = 2):
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

instructions = intcode(insList)
print('Day2:\n{}'.format(str(instructions[0])))


for ii in range(100):
    for jj in range(100):
        try:
            #TODO why do i have to import here?
            with open('day2_input.txt') as f:
                insList = list(map(int, f.read().rstrip('\n').split(",")))
            instructions = intcode(insList, ii, jj)
            if instructions[0] == 19690720:
                print(str(ii)+str(jj))
                break
        except:
            continue



