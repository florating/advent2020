"""Day 8: Treetop Tree House"""

from utils import read_input


def generate_trees_to_check(x, y, matrix):
    return {
        'top': [matrix[i][x] for i in range(y)][::-1],
        'bottom': [matrix[j][x] for j in range(y + 1, len(matrix))],
        'left': [matrix[y][k] for k in range(x)][::-1],
        'right': [matrix[y][l] for l in range(x + 1, len(matrix[0]))],
    }


def is_visible(tree, val, matrix):
    x, y = tree
    checks = generate_trees_to_check(x, y, matrix)

    for trees in checks.values():
        if val > max(map(int, trees)):
            return True

    return False


def count_perimeter(text):
    width = len(text[0])
    height = len(text)
    return (width + height - 2) * 2


def count_interior(matrix):
    """To access (x, y) in the tree drawing/matrix: matrix[y][x]"""
    count = 0
    trees = []
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if is_visible((x, y), int(matrix[y][x]), matrix):
                count += 1
                trees.append(int(matrix[y][x]))
    return count


def solve_p1(text):
    perimeter = count_perimeter(text)
    interior = count_interior(text)
    print(f'perimeter = {perimeter} and interior = {interior}')
    return perimeter + interior


def count_visible_trees(tree, lst):
    count = 0
    while count < len(lst):
        count += 1
        # print(f'Tree in lst is: {lst[count - 1]}')
        # print(f'tree: {tree}')
        if lst[count - 1] >= tree:
            break
    return count


def calculate_scenic_score(tree, val, matrix):
    x, y = tree
    directional_tree_lists = generate_trees_to_check(x, y, matrix)
    score = 1
    for trees in directional_tree_lists.values():
        score *= count_visible_trees(val, list(map(int, trees)))
    return score


def evaluate_interior(matrix):
    scores = []
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            scores.append(calculate_scenic_score((x, y), int(matrix[y][x]), matrix))
    return max(scores)


def solve_p2(text):
    return evaluate_interior(text)


if __name__ == '__main__':
    matrix = read_input('inputs/08.txt')
    print(solve_p1(matrix))
    print(solve_p2(matrix))
