"""Day 3: Binary Diagnostic"""

from pprint import pprint
from utils import read_input


"""Part 1"""


def calculate_gamma(nums):
    gamma = ''
    for bits in nums.values():
        gamma = gamma + count_mode(bits, is_common=True)
    return gamma


def calculate_epsilon(gamma_bin):
    """
    >>> calculate_epsilon('10110')
    '01001'
    """
    epsilon = ''
    for c in gamma_bin:
        if c == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    return epsilon


def convert_from_binary(binary_val):
    """Convert binary value to integer value, including leading 0s.
    >>> convert_from_binary('01001')
    9
    """
    value = 0
    binary_val = binary_val.lstrip('0')
    length = len(binary_val)
    for i, bit in enumerate(binary_val):
        if bit == '0':
            continue
        pos = length - i - 1
        value += 2 ** pos
    return value


def count_mode(inputs, is_common=True):
    """Return the mode from inputs (list of '0' and '1').
    If there are equal counts of '0' and '1', then return based on is_common's value.
    """
    seen = {}
    mode = most = None

    for num in inputs:
        if num not in seen:
            seen[num] = 0
        seen[num] += 1

    for key, val in seen.items():
        if val == len(inputs) / 2:
            return '1' if is_common else '0'
        if not most:
            mode, most = key, val
        if most and most < val:
            mode, most = key, val

    if is_common:
        return mode
    else:
        del seen[mode]
        return list(seen.keys())[0]


"""Part 2"""


def parse_input(file_input, is_part1=True, is_oxygen_rating=True):
    inputs = list(file_input)
    size = len(file_input[0])
    nums_by_pos = {}
    for i in range(size):
        nums_by_pos[i], current = [], []

        for bin_num in inputs:
            nums_by_pos[i].append(bin_num[i])

        if not is_part1:
            target = count_mode(nums_by_pos[i], is_common=is_oxygen_rating)
            for j, bit in enumerate(nums_by_pos[i]):
                if bit == target:
                    current.append(inputs[j])
            if len(current) == 1:
                return current[0]
            inputs = current
            pprint(inputs)
    else:
        print("Went through the entire input list.")
        return nums_by_pos


if __name__ == '__main__':
    # file = 'test03.txt'
    file = 'inputs/input03.txt'
    test = read_input(file, convert_to_int=False)

    values = parse_input(test, is_part1=True, is_oxygen_rating=False)
    gamma = calculate_gamma(values)
    epsilon = calculate_epsilon(gamma)
    print(convert_from_binary(gamma) * convert_from_binary(epsilon))

    print('\nStarting part 2...')
    oxygen = parse_input(test, is_part1=False, is_oxygen_rating=True)
    co2 = parse_input(test, is_part1=False, is_oxygen_rating=False)
    print(convert_from_binary(oxygen) * convert_from_binary(co2))
