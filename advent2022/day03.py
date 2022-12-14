"""Day 3: Rucksack Reorganization"""

from utils import read_input


def assign_priority(letter):
    """See more: https://docs.python.org/3/howto/unicode.html"""
    val = ord(letter)

    # Uppercase
    if 65 <= val <= 90:
        return val - 38

    # Lowercase
    return val - 96


def find_common_item_in_bag(line):
    mid = len(line) // 2
    a = set(line[:mid])
    b = set(line[mid:])
    return (a & b).pop()


def find_common_item_in_group(lst):
    a = set(lst[0])
    b = set(lst[1])
    c = set(lst[2])
    return (a & b & c).pop()


def solve_p1(file):
    text = read_input(file)
    items, priorities = [], 0
    for line in text:
        items.append(find_common_item_in_bag(line))
        priorities += assign_priority(items[-1])
    return priorities


def solve_p2(file):
    text = read_input(file)
    items, priorities, i = [], 0, 0

    while i < len(text):
        items.append(find_common_item_in_group(text[i:i+3]))
        priorities += assign_priority(items[-1])
        i += 3

    return priorities


if __name__ == '__main__':
    test = 'test_inputs/03.txt'
    input = 'inputs/03.txt'

    print(solve_p1(input))
    print(solve_p2(test))
