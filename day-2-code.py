'''
https://adventofcode.com/2019/day/2
'''


def intcode(instructions):
    '''
    list[0] == 1 :: list[list[3]] = list[list[1]] + list[list[2]]
    list[0] == 2 :: list[list[3]] = list[list[1]] * list[list[2]]
    list[0] == 99 :: return list
    '''
    instruction_count = len(instructions) // 4
    if len(instructions) % 4 != 0:
        instruction_count += 1
    for i in range(instruction_count):
        opcode_position = i * 4
        if instructions[opcode_position] == 99:
            return instructions
        elif instructions[opcode_position] == 1:
            instructions[instructions[opcode_position + 3]] = (
                instructions[instructions[opcode_position + 1]] +
                instructions[instructions[opcode_position + 2]]
            )
        elif instructions[opcode_position] == 2:
            instructions[instructions[opcode_position + 3]] = (
                instructions[instructions[opcode_position + 1]] *
                instructions[instructions[opcode_position + 2]]
            )
        else:
            raise KeyError(
                f'Illegal opcode value {instructions[opcode_position]} '
                f'at position {opcode_position}'
            )

def run_intcode():
    with open('day-2-input.txt', 'r') as f:
        data = f.readline().strip().split(',')
    data = [int(item) for item in data]
    data[1] = 12
    data[2] = 2
    result = intcode(data)
    return result[0]


def test_intcode():
    assert intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    assert intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]


if __name__ == '__main__':
    print(run_intcode())
