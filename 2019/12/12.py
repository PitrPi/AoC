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
