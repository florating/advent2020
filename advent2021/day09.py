"""Day 9: Smoke Basin"""


from pprint import pprint
from utils import read_input


def find_low_points(row, i):
    """Given a row from the floor map, return a list of (lows, index).
    >>> find_low_points('2199943210', 0)
    [(1, 0), (0, 0)]
    """
    almost_lows = []
    prev = row[0]
    for i, c in enumerate(row[1:-1]):
        next = row[i + 1]
        if i == 1 and prev < c:
            almost_lows.append((prev, i - 1))
        if prev > c and next > c:
            almost_lows.append((c, i))
    return almost_lows


def find_lows(floor_map):

    lows = []
    for row in floor_map:
        prev = row[0]
        was_dec = True
        for c in row[1:]:
            if prev < c and was_dec:
                lows.append(prev)
                was_dec = False


def check_directions(coord, row):
    x, y = coord
    if y > 0:
        up = (x, y + 1)
    if y < len(row) - 1:
        down = (x, y + 1)



if __name__ == '__main__':
    file = 'test_inputs/test09.txt'
    # file = 'inputs/input09.txt'
    floor = read_input(file)
    y = len(floor) - 1
    x = len(floor[0]) - 1
    vals = {}
    for i, row in enumerate(floor):
        vals[i] = find_low_points(row)
        print(vals)
        # check_directions(coord, row)
