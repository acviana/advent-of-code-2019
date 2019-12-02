'''
https://adventofcode.com/2019/day/1
'''


def fuel_counter_upper(mass):
    '''
    To find the fuel required for a module, take its mass, divide by
    three, round down, and subtract 2.
    '''
    return (mass // 3) - 2


def total_fuel_requirements():
    with open('day-1-input.txt', 'r') as f:
        data = f.readlines()
    data = [int(item.strip()) for item in data]
    data = [fuel_counter_upper(item) for item in data]
    print(sum(data))


def test_fuel_counter_upper():
    assert fuel_counter_upper(12) == 2
    assert fuel_counter_upper(14) == 2
    assert fuel_counter_upper(1969) == 654
    assert fuel_counter_upper(100756) == 33583


if __name__ == '__main__':
    total_fuel_requirements()
