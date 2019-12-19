from Helpers.helpers import read_newest
task = "task1"
task = "task2"


class Objects:

    def __init__(self, center, orbit):
        self.orbit = orbit
        self.center = center

    def call_center(self):
        self.connections = 1
        if self.center == "COM":
            return 1
        self.connections += objects[self.center].call_center()
        return self.connections

    def trace_path(self):
        if self.center == "COM":
            return ["COM"]
        self.path = [self.center] + (objects[self.center].trace_path())
        return self.path

data = read_newest()
# data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L' ]
objects = {"COM": Objects("COM", None)}
for dat in data:
    center, orbit = dat.split(")")
    objects[orbit] = Objects(center, orbit)

if task == 'part1':
    for obj in objects.values():
        obj.call_center()

    total = -1  # COM has 0 conn (but we init it with 1)
    for obj in objects.values():
        total += obj.connections
    print(total)
else:
    for obj in objects.values():
        obj.trace_path()

    santa_path = objects["SAN"].path
    my_path = objects["YOU"].path
    for i in santa_path:
        if i in my_path:
            intersection = i
            break

    my_path.index(intersection) + santa_path.index(intersection)