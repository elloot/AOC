import re


def __main__():
    puzzle_input = open('input.txt').read()
    operations = re.findall('([^\\d\\s]+) (\\d+)', puzzle_input)
    position = {'horizontal_pos': 0, 'depth': 0}
    aim = 0
    for (instruction, value) in operations:
        value = int(value)
        if instruction == 'forward':
            position['horizontal_pos'] += value
            position['depth'] += aim * value
        elif instruction == 'up':
            aim -= value
        elif instruction == 'down':
            aim += value
    print(position['horizontal_pos'] * position['depth'])


if __name__ == '__main__':
    __main__()
