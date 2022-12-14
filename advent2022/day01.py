"""Day 1: Calorie Counting"""


def read_list(lst):
    vals = []
    with open(lst, 'r') as f:
        curr = 0
        for line in f.readlines():
            if line in {'', '\n'}:
                vals.append(curr)
                curr = 0
            else:
                curr += int(line.strip())
    return vals


def parse_list(lst):
    elves, i = [], 0
    for val in lst:
        if type(val) is None:
            i += 1
        else:
            elves[i] += val
    elves[i] += val
    return elves


def solve_p1(elf_calories):
    return max(elf_calories)


if __name__ == '__main__':
    test_file = 'test_inputs/01.txt'
    file = 'inputs/01.txt'
    input = file

    # Solve part 1
    text = read_list(input)
    print(solve_p1(text))

    # Solve part 2
    top_three = sorted(text, reverse=True)[:3]
    print(sum(top_three))
