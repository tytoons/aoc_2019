import math
modules = open('day_01_data.txt').read().splitlines()

def getFuel(mass):
    return math.floor((mass / 3)) - 2

totalFuel = 0
for module in modules:
    fuel = getFuel(int(module))
    totalFuel += fuel
    while(fuel > 0):
        fuel = getFuel(fuel)
        if fuel > 0:
            totalFuel += fuel

print(totalFuel)
