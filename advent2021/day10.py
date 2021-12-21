"""Day 10: Syntax Scoring"""

from pprint import pprint

OPEN_BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

CLOSED = set(OPEN_BRACKETS.values())

CORRUPTION_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def is_corrupted(symbols):
    """Return True if incorrect closing bracket is found.
    >>> is_corrupted('<]')
    True
    """
    pass


def process_symbols(line):
    """Process a single line of symbols for either part 1 or part 2 of this coding challenge.
    Part 1: If the line is corrupted (ends in unexpected closing bracket), return the score.
    Part 2: If the line is incomplete, return a list of symbols needed to complete the chunks (close them) in the
        order required to close the chunks correctly.
    """
    expected = []
    for symbol in line:
        if symbol in OPEN_BRACKETS:
            expected.append(OPEN_BRACKETS[symbol])
        else:
            next = expected.pop()
            if symbol != next and symbol in CLOSED:
                # print(f'\nOops; expected {next} but found {symbol} instead!')
                return CORRUPTION_POINTS[symbol]  # for part 1

    if expected:  # for part 2
        return expected[::-1]


def solve(lines, is_part2=False):
    score = [] if is_part2 else 0
    for i, line in enumerate(lines):
        value = process_symbols(line)
        if not is_part2 and value and isinstance(value, int):
            score += value
            # print(f'for i = {i}: value = {value} & total score = {score}')
        elif is_part2 and value and isinstance(value, list):
            score.append(calculate_completion_score(value))
    if is_part2:
        score.sort()
        # pprint(score)
        return score[(len(score)//2)]
    else:
        return score


def calculate_completion_score(completion_string):
    """Return the completion score.
    >>> calculate_completion_score('}}]])})]')
    288957
    """
    score = 0
    for symbol in completion_string:
        score *= 5
        score += AUTOCOMPLETE_POINTS[symbol]
    print(f'for {completion_string}: score = {score}')
    return score


if __name__ == '__main__':
    file = 'inputs/input10.txt'
    # file = 'test_inputs/test10.txt'
    data = []
    with open(file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    score = solve(data, is_part2=True)
    print(f'middle score = {score}')
