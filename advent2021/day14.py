"""Day 14: Extended Polymerization"""


from pprint import pprint


def parse_input(file):
    """Return starting polymer template (start) and pair insertion rules (codes)."""
    start = ''
    codes = {}
    with open(file, 'r') as f:
        start = f.readline().strip()
        for line in f.readlines():
            if not line.strip():
                continue
            a, b = line.strip().split(' -> ')
            codes[a] = b
    return start, codes


def polymerize(num_cycles, template, rules):
    count = 0
    while count < num_cycles:
        i = 0
        progress = template[0]
        while i < len(template) - 1:
            pair = template[i:i + 2]
            progress += rules.get(pair, '') + pair[1]
            i += 1
            # print(progress)
        count += 1
        template = progress
    return progress


def count_elements(polymer):
    counts = {}
    for c in polymer:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts


def get_most_least(counts):
    most_pair, least_pair = None, None
    most, least = None, None
    for key, value in counts.items():
        if not most or not least:
            most = least = value
            most_pair = least_pair = key
        if value > most:
            most = value
            most_pair = key
        elif value < least:
            least = value
            least_pair = key
    return most - least


def find_redundancies(codes):
    """Maybe use for part 2?"""
    no_repeats = {}
    for key, val in codes.items():
        if val not in no_repeats:
            no_repeats[val] = set()
        no_repeats[val].add(key)
    return no_repeats


if __name__ == '__main__':
    # file = 'test_inputs/test14.txt'
    file = 'inputs/input14.txt'

    start, codes = parse_input(file)
    # pprint(codes)
    # pprint(find_redundancies(codes))

    answer = polymerize(10, start, codes)
    # print(len(answer))
    print(get_most_least(count_elements(answer)))
