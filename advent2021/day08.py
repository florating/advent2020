"""Day 8: Seven Segment Search"""


from pprint import pprint


NUM_SEGMENTS = {
    1: 'cf',
    4: 'bcdf',
    7: 'acf',
    8: 'abcdefg',
}

ALL_NUMS = {
    8: 'acedgfb',   # 7
    5: 'cdfbe',     # 5
    2: 'gcdfa',     # 5
    3: 'fbcad',     # 5
    7: 'dab',       # 3
    9: 'cefabd',    # 6
    6: 'cdfgeb',    # 6
    4: 'eafb',      # 4
    0: 'cagedb',    # 6
    1: 'ab',        # 2
}

SPECIAL_LENGTHS = { len(value): key for key, value in NUM_SEGMENTS.items() }


def get_output_values(file):
    outputs = []
    with open(file, 'r') as f:
        for line in f.readlines():
            _, output = line.strip().split('|')
            # print(output)
            outputs.append(output.strip().split(' '))
    return outputs


def count_nums(notes):
    """Count the # of times 1, 4, 7, and 8 appear."""
    count = 0
    for note in notes:
        for code in note:
            if len(code) in SPECIAL_LENGTHS.keys():
                count += 1
    return count


def get_codes(length, is_list=False, data=ALL_NUMS):
    if is_list:
        return {}
    else:
        return {digit: code for digit, code in data.items() if len(code) == length}


def get_entry_values(file):
    entries = []
    with open(file, 'r') as f:
        for line in f.readlines():
            entry, _ = line.strip().split('|')
            entries.append(entry.strip().split(' '))
    return entries


def decode_entry(entry):
    """For each line in input (entry), determine wire/segment connections and decode the output values."""
    code = {}
    for e in entry:
        length = len(e)
        if length in SPECIAL_LENGTHS.keys():
            digit = SPECIAL_LENGTHS[length]
            code[digit] = e
    length5 = get_codes(5)
    length6 = get_codes(6)
    print(length5)
    return code


if __name__ == '__main__':
    file = 'test_inputs/test08.txt'
    # file = 'input08.txt'
    output = get_output_values(file)
    print(output)
    print(count_nums(output))

    entries = get_entry_values(file)
    for e, o in zip(entries, output):
        decode_entry(e)
