from Helpers.helpers import read_newest


class Ship:

    DIRECTION_ORDER = ['N', 'E', 'S', 'W']

    def __init__(self, facing="E", waypoint=None):
        self.facing = facing
        self.x = 0
        self.y = 0
        self.waypoint = waypoint

    # Part 1
    def move(self, instruction):
        direction, steps = self.parse_instruction(instruction)
        if direction == 'F':
            direction = self.facing
        if direction == 'E':
            self.x += steps
        elif direction == 'W':
            self.x -= steps
        elif direction == 'N':
            self.y += steps
        elif direction == 'S':
            self.y -= steps
        elif direction == 'L':
            self.facing = self.DIRECTION_ORDER[
                (self.DIRECTION_ORDER.index(self.facing) - steps//90)
                % len(self.DIRECTION_ORDER)
            ]
        elif direction == 'R':
            self.facing = self.DIRECTION_ORDER[
                (self.DIRECTION_ORDER.index(self.facing) + steps//90)
                % len(self.DIRECTION_ORDER)
                ]

    @staticmethod
    def parse_instruction(instruction):
        return instruction[0], int(instruction[1:])

    def calculate_distance(self):
        return abs(self.x) + abs(self.y)

    # Part 2
    def move_waypoint(self, instruction):
        direction, steps = self.parse_instruction(instruction)
        if direction == 'F':
            self.x += self.waypoint[0]*steps
            self.y += self.waypoint[1]*steps
        if direction == 'E':
            self.waypoint[0] += steps
        elif direction == 'W':
            self.waypoint[0] -= steps
        elif direction == 'N':
            self.waypoint[1] += steps
        elif direction == 'S':
            self.waypoint[1] -= steps
        elif direction == 'L':
            for _ in range(steps//90):
                if self.waypoint[0] > 0 == self.waypoint[1] > 0:
                    self.waypoint = [self.waypoint[1], -self.waypoint[0]]
                else:
                    self.waypoint = [-self.waypoint[1], self.waypoint[0]]

        elif direction == 'R':
            for _ in range(steps//90):
                if self.waypoint[0] > 0 == self.waypoint[1] > 0:
                    self.waypoint = [-self.waypoint[1], self.waypoint[0]]
                else:
                    self.waypoint = [self.waypoint[1], -self.waypoint[0]]


if __name__ == '__main__':
    data = read_newest()
    # Task 1
    ship = Ship()
    for dat in data:
        ship.move(dat)
    print(ship.calculate_distance())

    # Task 2
    ship_waypoint = Ship(waypoint=[10, 1])
    for dat in data:
        ship_waypoint.move_waypoint(dat)
        # print(ship_waypoint.x)
        # print(ship_waypoint.y)
        # print(ship_waypoint.waypoint)
    print(ship_waypoint.calculate_distance())
