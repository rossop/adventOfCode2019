def read_input():
    """
    Read input from a text file
    :return: :insList: list of instructions
    """
    orbitList = {}
    with open('day06_input.txt') as f:
        for line in f:
            planet, satellite = line.split(')')
            satellite = satellite.rstrip('\n')

            if planet in orbitList:
                orbitList[planet].append(satellite)
            else:
                orbitList[planet] = [satellite]

    return orbitList

def part_one():
    """
    Counts the number of orbitating planets
    :return: Val:: number of orbitating planets
    """
    orbitList = read_input() # direct only

    print(len(orbitList.keys()))

part_one()
