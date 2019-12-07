def read_input():
    """
    Read input from a text file
    :return: :insList: list of instructions
    """
    orbitDict = {}
    with open('day06_input.txt') as f:
        for line in f:
            planet, satellite = line.split(')')
            satellite = satellite.rstrip('\n')

            if satellite in orbitDict:
                orbitDict[satellite].append(planet)
            else:
                orbitDict[satellite] = [planet]

    return orbitDict

def does_orbit(satellite, planetsDict, dest = 'COM'):
    count = 0
    orbiting_planets = []
    if satellite != dest:
        if satellite in planetsDict.keys():
            for planet in planetsDict[satellite]:
                count += 1
                orbiting_planets.append(planet)
                does_orbit_count, does_orbit_orbits = does_orbit(planet,planetsDict,dest)
                count += does_orbit_count
                orbiting_planets += does_orbit_orbits

    return count, orbiting_planets
    
def independent_orbits(planetsDict):
    ind_orbit = 0
    for satellite, planets in planetsDict.items():
        for planet in planets:
            if planet in planetsDict.keys(): #it's also a satellite of another planet
                does_orbit_count, does_orbit_orbits = does_orbit(planet, planetsDict)
                ind_orbit += does_orbit_count

    return ind_orbit

def num_of_orbits(orbitDict):
    """
    Counts the number of orbitating planets
    :return: Val:: number of orbitating planets
    """

    total_orbits = len(orbitDict.keys())
    total_orbits += independent_orbits(orbitDict)

    return total_orbits

def meet_santa(orbitDict):
    """
    This function identify on which orbits it is possible to meet santa with the least number of jumps
    :return: int, number of jumps
    """
    santa_count, santa_path  = does_orbit('SAN', orbitDict)
    your_count, your_path = does_orbit('YOU', orbitDict)
    santa_planets = set(santa_path)
    your_planets = set(your_path)
    common = len(santa_planets.intersection(your_planets))
    dist = santa_count + your_count - 2*common
    return dist


orbitDict = read_input() # direct orbits only
print(num_of_orbits(orbitDict))
print(meet_santa(orbitDict))