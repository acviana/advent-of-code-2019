'''
https://adventofcode.com/2019/day/3#
'''


class Wire:

    def __init__(self, instructions):
        self.instructions = instructions.split(',')
        self.current_position = (0, 0)
        self.wire_route = []

    def next_position(self, instruction):
        direction = instruction[0]
        magnitude = int(instruction[1:])
        if direction == 'L':
            self.current_position = (
                self.current_position[0] - magnitude,
                self.current_position[1]
            )
        elif direction == 'R':
            self.current_position = (
                self.current_position[0] + magnitude,
                self.current_position[1]
            )
        elif direction == 'U':
            self.current_position = (
                self.current_position[0],
                self.current_position[1] + magnitude
            )
        elif direction == 'D':
            self.current_position = (
                self.current_position[0],
                self.current_position[1] - magnitude
            )
        else:
            raise KeyError(f'Unexpected instricution direction {instruction}')
        return self.current_position

    def route(self):
        return [
            self.next_position(instruction) for instruction in self.instructions
        ]


def find_overlap(wire1, wire2):
    wire1_path = wire1.route()
    wire2_path = wire2.route()
    overlap = set(wire1_path).intersection(wire2_path)
    return [item for item in overlap]


def test_wire_class():
    wire = Wire('R75,D30,R83,U83,L12,D49,R71,U7,L72')
    assert wire.instructions == ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    # assert wire.route() == [(75, 0), (75, -30), (158, -30)]
    assert isinstance(wire.instructions, list)

    wire = Wire('L1,R1,U1,D1')
    wire_route = wire.route()
    assert wire_route == [(-1, 0), (0, 0), (0, 1), (0, 0)]


def test_find_overlap():
    wire1 = Wire('U1,D1')
    wire2 = Wire('D1,U1')
    assert (0, 0) in find_overlap(wire1, wire2)

    wire1 = Wire('R75,D30,R83,U83,L12,D49,R71,U7,L72')
    wire2 = Wire('U62,R66,U55,R34,D71,R55,D58,R83')
    assert len(find_overlap(wire1, wire2)) == 2


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
    overlap = find_overlap(wire1, wire2)
    return (
        abs(overlap[0][0] - overlap[1][0]) +
        abs(overlap[0][1] - overlap[1][1])
    )


if __name__ == '__main__':
    wire = Wire('R75,D30,R83,U83,L12,D49,R71,U7,L72')
    print(wire.instructions)
