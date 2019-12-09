'''
https://adventofcode.com/2019/day/3#
'''


class Wire:

    def __init__(self, instructions):
        self.instructions = instructions.split(',')
        self.wire_route = [(0,0)]

    def next_position(self, instruction):
        direction = instruction[0]
        magnitude = int(instruction[1:])
        if direction == 'L':
            for step in range(magnitude):
                self.wire_route += [(
                    self.wire_route[-1][0] - 1,
                    self.wire_route[-1][1]
                )]
        elif direction == 'R':
            for step in range(magnitude):
                self.wire_route += [(
                    self.wire_route[-1][0] + 1,
                    self.wire_route[-1][1]
            )]
        elif direction == 'U':
            for step in range(magnitude):
                self.wire_route += [(
                    self.wire_route[-1][0],
                    self.wire_route[-1][1] + 1
            )]
        elif direction == 'D':
            for step in range(magnitude):
                self.wire_route += [(
                    self.wire_route[-1][0],
                    self.wire_route[-1][1] - 1
            )]
        else:
            raise KeyError(f'Unexpected instruction direction {instruction}')

    def route(self):
        [self.next_position(instruction) for instruction in self.instructions]
        return self.wire_route


def find_overlap(wire1, wire2):
    overlap = set(wire1.route()).intersection(wire2.route())
    return [item for item in overlap if item != (0, 0)]


def test_wire_class():
    wire = Wire('L1,R1,U1,D1')
    assert wire.route() == [(0, 0), (-1, 0), (0, 0), (0, 1), (0, 0)]

    wire = Wire('U2,R2')
    assert wire.route() == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]


def test_find_overlap():
    wire1 = Wire('U1,D1')
    wire2 = Wire('D1,U1')
    assert [] == find_overlap(wire1, wire2)

    wire1 = Wire('U2,R2')
    wire2 = Wire('R2,U2')
    assert [(2, 2)] == find_overlap(wire1, wire2)


def test_main():
    assert (
        main(
            'R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83'
        ) == 159
    )
    assert (
        main(
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        ) == 135
    )


def main(instructions1, instructions2):
    wire1 = Wire(instructions1)
    wire2 = Wire(instructions2)
    overlap_list = find_overlap(wire1, wire2)
    overlap_distances = [abs(item[0]) + abs(item[1]) for item in overlap_list]
    return min(overlap_distances)


if __name__ == '__main__':
    with open('day-3-input.txt', 'r') as f:
        data = f.readlines()
    print(f'Distance is {main(data[0].strip(), data[1].strip())}')
