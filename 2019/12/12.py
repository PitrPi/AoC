from itertools import combinations
io = {'x': 4, 'y': 1, 'z': 1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
europa = {'x': 11, 'y': -18, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
ganymedes = {'x': -2, 'y': -10, 'z': -4, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
callisto = {'x': -7, 'y': -2, 'z': 14, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# io = {'x': -1, 'y': 0, 'z': 2, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# europa = {'x': 2, 'y': -10, 'z': -7, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# ganymedes = {'x': 4, 'y': -8, 'z': 8, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# callisto = {'x': 3, 'y': 5, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
moons = {'io': io, 'europa': europa, 'ganymedes': ganymedes, 'callisto': callisto}
axis = ['x', 'y', 'z']

for _ in range(1000):
    for moon1, moon2 in combinations(moons.keys(), 2):
        for axe in axis:
            if moons[moon1][axe] < moons[moon2][axe]:
                moons[moon1][axe+"_vel"] += 1
                moons[moon2][axe+"_vel"] -= 1
            elif moons[moon1][axe] > moons[moon2][axe]:
                moons[moon1][axe+"_vel"] -= 1
                moons[moon2][axe+"_vel"] += 1
    for moon in moons:
        for axe in axis:
            moons[moon][axe] += moons[moon][axe+"_vel"]

total_energy = 0
for moon in moons:
    pot = 0
    kin = 0
    for axe in axis:
        pot += abs(moons[moon][axe])
        kin += abs(moons[moon][axe+"_vel"])
    total_energy += pot*kin
print(total_energy)
from itertools import combinations
io = {'x': 4, 'y': 1, 'z': 1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
europa = {'x': 11, 'y': -18, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
ganymedes = {'x': -2, 'y': -10, 'z': -4, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
callisto = {'x': -7, 'y': -2, 'z': 14, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# io = {'x': -1, 'y': 0, 'z': 2, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# europa = {'x': 2, 'y': -10, 'z': -7, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# ganymedes = {'x': 4, 'y': -8, 'z': 8, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# callisto = {'x': 3, 'y': 5, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
moons = {'io': io, 'europa': europa, 'ganymedes': ganymedes, 'callisto': callisto}
axis = ['x', 'y', 'z']

cycle_x = 0
cycle_y = 0
cycle_z = 0
x_set = set()
y_set = set()
z_set = set()
found_x = False
found_y = False
found_z = False


while not(found_x and found_y and found_z):
    x_set_current = tuple([(moons[moon]['x'], moons[moon]['x_vel']) for moon in moons])
    y_set_current = tuple([(moons[moon]['y'], moons[moon]['y_vel']) for moon in moons])
    z_set_current = tuple([(moons[moon]['z'], moons[moon]['z_vel']) for moon in moons])
    if found_x:
        pass
    elif x_set_current in x_set:
        print("found_x")
        x_repeat = x_set_current
        found_x = True
    else:
        x_set.add(x_set_current)
    if found_y:
        pass
    elif y_set_current in y_set:
        print("found_y")
        y_repeat = y_set_current
        found_y = True
    else:
        y_set.add(y_set_current)
    if found_z:
        pass
    elif z_set_current in z_set:
        print("found_z")
        z_repeat = z_set_current
        found_z = True
    else:
        z_set.add(z_set_current)
    for moon1, moon2 in combinations(moons.keys(), 2):
        for axe in axis:
            if moons[moon1][axe] < moons[moon2][axe]:
                moons[moon1][axe+"_vel"] += 1
                moons[moon2][axe+"_vel"] -= 1
            elif moons[moon1][axe] > moons[moon2][axe]:
                moons[moon1][axe+"_vel"] -= 1
                moons[moon2][axe+"_vel"] += 1
    for moon in moons:
        for axe in axis:
            moons[moon][axe] += moons[moon][axe+"_vel"]
    if not found_x:
        cycle_x += 1
    if not found_y:
        cycle_y += 1
    if not found_z:
        cycle_z += 1


io = {'x': 4, 'y': 1, 'z': 1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
europa = {'x': 11, 'y': -18, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
ganymedes = {'x': -2, 'y': -10, 'z': -4, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
callisto = {'x': -7, 'y': -2, 'z': 14, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# io = {'x': -1, 'y': 0, 'z': 2, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# europa = {'x': 2, 'y': -10, 'z': -7, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# ganymedes = {'x': 4, 'y': -8, 'z': 8, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
# callisto = {'x': 3, 'y': 5, 'z': -1, 'x_vel': 0, 'y_vel': 0, 'z_vel': 0}
moons = {'io': io, 'europa': europa, 'ganymedes': ganymedes, 'callisto': callisto}
axis = ['x', 'y', 'z']

found_x = False
found_y = False
found_z = False
while not(found_x and found_y and found_z):
    x_set_current = tuple([(moons[moon]['x'], moons[moon]['x_vel']) for moon in moons])
    y_set_current = tuple([(moons[moon]['y'], moons[moon]['y_vel']) for moon in moons])
    z_set_current = tuple([(moons[moon]['z'], moons[moon]['z_vel']) for moon in moons])
    if found_x:
        pass
    elif x_set_current == x_repeat:
        print("found_x_start")
        found_x = True
    if found_y:
        pass
    elif y_set_current == y_repeat:
        print("found_y_start")
        found_y = True
    if found_z:
        pass
    elif z_set_current == z_repeat:
        print("found_z_start")
        found_z = True
    for moon1, moon2 in combinations(moons.keys(), 2):
        for axe in axis:
            if moons[moon1][axe] < moons[moon2][axe]:
                moons[moon1][axe+"_vel"] += 1
                moons[moon2][axe+"_vel"] -= 1
            elif moons[moon1][axe] > moons[moon2][axe]:
                moons[moon1][axe+"_vel"] -= 1
                moons[moon2][axe+"_vel"] += 1
    for moon in moons:
        for axe in axis:
            moons[moon][axe] += moons[moon][axe+"_vel"]
    if not found_x:
        cycle_x -= 1
    if not found_y:
        cycle_y -= 1
    if not found_z:
        cycle_z -= 1


import math
def lcm(num1, num2):
    return abs(num1*num2) // math.gcd(num1, num2)
print(lcm(cycle_z, lcm(cycle_x, cycle_y)))