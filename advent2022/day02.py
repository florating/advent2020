"""Day 2: Rock Paper Scissors"""

from utils import read_input

POINTS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

CODE = {
    'rock': {'A', 'X'},
    'paper': {'B', 'Y'},
    'scissors': {'C', 'Z'},
}

DESIRED_OUTCOME = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

CODE_TO_WORD = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors',
}

WINS_AGAINST = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock',
}

LOSES_AGAINST = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}


def parse_input(file, p1=True):
    """Returns a list of moves translated into words in this format: (opponent_move, your_move)."""
    text = read_input(file, False)
    moves = []
    for line in text:
        opponent = CODE_TO_WORD[line[0]]
        you = CODE_TO_WORD[line[-1]] if p1 else DESIRED_OUTCOME[line[-1]]
        moves.append((opponent, you))
    return moves


def score(move):
    opp, you = move
    pts = 0
    if LOSES_AGAINST[you] == opp:
        pts = 6
    elif you == opp:
        pts = 3
    return pts + POINTS[you]


def score_points(text):
    pts = 0
    for line in text:
        pts += score(line)
    return pts


def solve_p1(file):
    text = parse_input(file)
    pts = 0
    for line in text:
        pts += score(line)
    return pts


def decode_your_move(move):
    opp_move, outcome = move
    if outcome == 'draw':
        your_move = opp_move
    elif outcome == 'lose':
        your_move = LOSES_AGAINST[opp_move]
    else:
        your_move = WINS_AGAINST[opp_move]
    return opp_move, your_move


def decode_all_moves(text):
    moves = []
    for line in text:
        moves.append(decode_your_move(line))
    return moves


def solve_p2(file):
    text = parse_input(file, p1=False)
    moves = decode_all_moves(text)
    return score_points(moves)


if __name__ == '__main__':
    test = 'test_inputs/02.txt'
    input = 'inputs/02.txt'
    print(f'Answer to part 1: {solve_p1(input)}')
    print(f'Answer to part 2: {solve_p2(input)}')
