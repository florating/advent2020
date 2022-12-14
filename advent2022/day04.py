"""Day 4: Camp Cleanup"""


def read_and_parse_input(file):
    lst = []
    tuplify = lambda elf_range: tuple(map(int, elf_range.split('-')))

    with open(file, 'r') as f:
        for line in f.readlines():
            # Takes input in the form of '2-4,6-8' and parses into [(2, 4), (6, 8)]
            lst.append(list(map(tuplify, line.strip().split(','))))
    return lst


def contains_other_section(this, other):
    # Check if remotely possible that one range is contained within the other
    # print(f'this section: {this}')
    # print(f'other section: {other}')

    if other[1] >= this[0] and other[0] >= this[0]:
        if other[0] <= this[1] and other[1] <= this[1]:
            # print(f'Yep! {this} contains {other}')
            return True
        else:
            return False


def contains_partial_overlap(this, other):
    if contains_other_section(this, other):
        return True

    if this[0] <= other[1] <= this[1]:
        print(f'Yep! {this} contains {other[0]}')
        return True

    elif this[0] <= other[0] <= this[1]:
        print(f'Yep! {this} contains {other[0]}')
        return True
    else:
        return False


def solve_p1(text):
    count = 0
    for a, b in text:
        if contains_other_section(a, b) or contains_other_section(b, a):
            count += 1
    return count


def solve_p2(text):
    count = 0
    for a, b in text:
        if contains_partial_overlap(a, b) or contains_partial_overlap(b, a):
            count += 1
    return count


if __name__ == '__main__':
    test = 'test_inputs/04.txt'
    input = 'inputs/04.txt'

    text = read_and_parse_input(input)
    print(solve_p1(text))
    print(solve_p2(text))
