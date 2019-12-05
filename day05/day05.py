import urllib

def download_input():
    """
    TODO: upgrade so that now on you don't need to dowload imputs, and make it a general file you can run from every
        problem
    :return: input as list
    """
    link = "https://adventofcode.com/2019/day/5/input"
    with urllib.request.urlopen(link) as f:
        input = f.read()
        print(input)
    ##

def read_input():
    """
    Read input from a text file
    :return: :insList: list of instructions
    """
    with open('day5_input.txt') as f:
        insList = list(map(int, f.read().rstrip('\n').split(",")))

    return insList




def run_program(insList, noun = 12, verb = 2):
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
                it += 4

            elif opcode == 2:
                insList[dest] = op1 * op2
                it += 4

            elif opcode == 3:
                dest = inslist[it+1]
                inslist[dest] = dest

            else:
                print('ERROR: undefined opcode')
                break


    return insList
download_input()