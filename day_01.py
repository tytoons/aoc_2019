import math
modules = open('day_01_data.txt').read().splitlines()

def getFuel(mass):
    return math.floor((mass / 3)) - 2

totalFuel = 0
for module in modules:
    totalFuel += getFuel(int(module))

print(totalFuel)
