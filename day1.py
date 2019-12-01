# day 1
import math

def day1():

    with open('day1_input.txt') as f:
        masses = f.readlines()

    fuel = 0
    for mass in masses:
        need_more_mass = True
        m = mass
        while need_more_mass:
            m = fuelCalc(m)
            if m > 0:
                fuel += m
            else:
                need_more_mass = False
    return fuel

def fuelCalc(mass):
    """ Calculates Fuel mass necessary to move a specific mass """
    return math.floor(int(mass)/3)-2

fuel = day1()
print('Day1:\n{}'.format(str(fuel)))