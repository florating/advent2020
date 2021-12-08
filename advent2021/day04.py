"""Day 4: Giant Squid"""


from pprint import pprint


def get_bingo_numbers(file_input):
    """Return a list of ints representing drawn numbers to play bingo."""
    nums = None
    with open(file_input, 'r') as f:
        nums = f.readline().strip()
    return list(map(int, nums.split(',')))


def get_boards(file_input):
    boards = []
    with open(file_input, 'r') as f:
        board = []
        for line in f.readlines():
            line = line.strip()
            if not line or ',' in line:
                if board:
                    boards.append(board)
                board = []
                continue
            row = list(map(int, line.split()))
            board.append(row)
    if board:
        boards.append(board)
    return boards


def is_winner(board):
    """Given a 2D matrix of ints (board), check if any rows or columns are complete."""
    for row in board:
        if all(row):
            return True
    for values in zip(*board):
        if all(values):
            return True
    return False


def create_empty_board(board):
    """Create empty boards to mark values while playing the game."""
    x = len(board[0])
    col = list(zip(board))
    y = len(col)
    return [[0 for _x in range(x)] for _y in range(y)]


def setup_boards(boards):
    all_boards = {}
    for i, board in enumerate(boards):
        all_boards[i] = {
            'numbers': board,
            'marked': create_empty_board(board)
        }
    return all_boards


def check_board(board, board_to_mark, num):
    """Check if num is on the board, marks the board_to_mark if present, returns T/F."""
    x, y = None, None
    for i, row in enumerate(board):
        if num in row:
            x = i
            y = row.index(num)
            # print(f'Found {num} in the board! at x = {x} and y = {y}')
            board_to_mark[x][y] = num
            return True
    return False


def calculate_score(board, board_to_mark, num):
    """Upon winning the game: calculate sum of unmarked numbers and multiply by num."""
    total = 0
    for row_a, row_b in zip(board, board_to_mark):
        for a, b in zip(row_a, row_b):
            if not b:
                total += a
                # print(f'The running total for the score is: {total}')
    return total * num


def play_bingo(file, is_part2=False):
    drawn_nums = get_bingo_numbers(file)
    print(f'drawn_nums = {drawn_nums}')
    boards = get_boards(file)
    all_boards = setup_boards(boards)
    original_boards = dict(all_boards)
    completed = set()
    for num in drawn_nums:
        # print(f'The number drawn is: {num}')
        for key, board in original_boards.items():
            if board and key not in completed:
                numbers = all_boards[key]['numbers']
                to_mark = all_boards[key]['marked']
                if check_board(numbers, to_mark, num):
                    if is_winner(to_mark):
                        print('Yay, we have a winner!')
                        if len(all_boards) == 1 and is_part2:
                            return calculate_score(numbers, to_mark, num)
                        elif is_part2:
                            del all_boards[key]
                            completed.add(key)
                        else:
                            return calculate_score(numbers, to_mark, num)
    return 'Went through the entire game without a winner...'


if __name__ == '__main__':
    # file = 'test04.txt'
    file = 'input04.txt'
    print(play_bingo(file, is_part2=True))
