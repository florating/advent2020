"""Day 2: Dive!"""


from day01 import read_input


def parse_dirs(dirs):
    """Currently set up to solve for part 2."""
    aim, horiz, depth = 0, 0, 0
    for d in dirs:
        direction, value = d.split(' ')
        value = int(value)
        if direction == 'forward':
            horiz += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    return horiz, depth


if __name__ == '__main__':
    # file = 'test02.txt'
    file = 'input02.txt'
    lst = read_input(file)
    (horiz, depth) = parse_dirs(lst)
    print(horiz * depth)
