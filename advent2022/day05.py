"""Day 5: Supply Stacks"""


def read_input(file):
    text = []
    with open(file, 'r') as f:
        for line in f.readlines():
            text.append(line.strip('\n'))
    return text


def draw_matrix(width, crates):
    """
            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

        c: 1   5   9
        n: 0   1   2

        c(n) = 1 + 4n
    """
    matrix = [[] for _ in range(width)]
    for row in crates[::-1]:
        max_len, col = len(row), 0
        while col < width:
            pos = 4 * col + 1
            if pos < max_len:
                if row[pos] != ' ':
                    matrix[col].append(row[pos])
                col += 1
            else:
                break
    return matrix


def move_crate(matrix, col_a, col_b):
    """Move a crate off of col_a and place on top of col_b."""
    crate = matrix[col_a - 1].pop()
    matrix[col_b - 1].append(crate)
    return matrix


def move_crates(matrix, num_crates, col_a, col_b):
    """Move crates off of col_a and place on top of col_b while retaining original stacked order."""
    crates = matrix[col_a - 1][-num_crates:]
    for i in range(num_crates):
        matrix[col_a - 1].pop()
    matrix[col_b - 1].extend(crates)
    return matrix


def parse_instructions(file):
    text = []
    with open(file, 'r') as f:
        for line in f.readlines():
            # print(line)
            num_crates, cols = line.strip('move\n').split(' from ')
            a, *chars, b = cols
            text.append([int(num_crates.strip()), (int(a), int(b))])
            # print(f'num_crates: {num_crates}')
            # print(f'cols: {cols}')
            # print(text[-1])
    return text


def run_program(matrix, instructions, p1=True):
    for num_crates, cols in instructions:
        if p1 or num_crates == 1:
            for i in range(num_crates):
                matrix = move_crate(matrix, cols[0], cols[1])
        else:
            matrix = move_crates(matrix, num_crates, cols[0], cols[1])
    return matrix


def print_ends(matrix):
    ends = ''
    for i in range(len(matrix)):
        ends += matrix[i][-1]
    return ends


if __name__ == '__main__':
    test_crates = 'test_inputs/05_crates.txt'
    crates = 'inputs/05_crates.txt'

    # Testing
    # text = read_input(test_crates)
    # instructions = parse_instructions('test_inputs/05_instructions.txt')
    # matrix = draw_matrix(3, text)

    # Actual
    text = read_input(crates)
    instructions = parse_instructions('inputs/05_instructions.txt')
    matrix = draw_matrix(9, text)

    # Solve for part 2
    matrix = run_program(matrix, instructions, p1=False)
    ends = print_ends(matrix)
    print(ends)
