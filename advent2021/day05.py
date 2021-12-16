"""Day 5: Hydrothermal Venture"""


from pprint import pprint
from utils import read_input


def parse_input(lines):
    inputs = []
    x_values, y_values = set(), set()
    for line in lines:
        coords = line.split(' -> ')
        inputs.append([])
        for coord in coords:
            value = tuple(map(int, coord.split(',')))
            x_values.add(value[0])
            y_values.add(value[1])
            inputs[-1].append(value)

    return inputs, draw_map(max(x_values), max(y_values))


def draw_map(x_coord, y_coord):
    return [[0 for _x in range(x_coord + 1)] for _y in range(y_coord + 1)]


def draw_lines(matrix, start, end):
    """Increment value of each position in the matrix to represent # of lines.
    eg: (2, 2), (2, 1)
    """
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        # vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            matrix[y][x1] += 1
    elif y1 == y2:
        # horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            matrix[y1][x] += 1
    else:
        # diagonal line at 45 degree angle
        x_is_dec = True if (x2 - x1) < 0 else False
        y_is_dec = True if (y2 - y1) < 0 else False
        x, y = x1, y1
        while True:
            matrix[x][y] += 1
            if x == x2:
                break
            x += -1 if x_is_dec else 1
            y += -1 if y_is_dec else 1
            # if y_is_dec:
            #     y -= 1
            #     if y < y2:
            #         break
            # else:
            #     y += 1
            #     if y > y2:
            #         break


def count_overlap(matrix):
    count = 0
    for row in matrix:
        for val in row:
            if val >= 2:
                count += 1
    return count


if __name__ == '__main__':
    file = 'test_inputs/test05.txt'
    # file = 'input05.txt'
    lines = read_input(file)
    coords, matrix = parse_input(lines)
    for a, b in coords:
        draw_lines(matrix, a, b)
    # print(coords)
    # pprint(matrix)
    print(count_overlap(matrix))
