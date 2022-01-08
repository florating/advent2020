"""Day 13: Transparent Origami"""

# import os
# import sys
# import inspect
#
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

from pprint import pprint

import pandas as pd

"""
example points:
6,10
0,14
9,10
0,3

xdict = {
    0: {3, 14},
    6: {10},
    9: {10},
}

ydict = {
    3: {0},
    10: {6, 9},
    14: {0},
}
"""


def initialize(filepath):
    x_to_y = {}  # keys = x-values; paired values = sets of y-values with dots
    y_to_x = {}
    is_initialized = False
    folds = []

    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            # print(line)
            if not line:
                is_initialized = True
                continue

            if not is_initialized:
                x, y = line.strip().split(',')
                x, y = int(x), int(y)
                if x not in x_to_y:
                    x_to_y[x] = set()
                if y not in y_to_x:
                    y_to_x[y] = set()
                x_to_y[x].add(y)
                y_to_x[y].add(x)
            else:
                text, num = line.split('=')
                axis = text[-1]
                folds.append((axis, int(num)))

    return x_to_y, y_to_x, folds


def run_program(xdict_original, ydict_original, folds):
    xdict, ydict = xdict_original, ydict_original
    for i, fold in enumerate(folds):
        axis, num = fold
        print(f'fold at {axis}={num}')
        # print(f'starting with xdict = ')
        # pprint(xdict)
        # print(f'and ydict = ')
        # pprint(ydict)
        xdict, ydict = fold_paper(axis, num, xdict, ydict)
        print(f'at step {i}: there are {count_points(xdict)} points on the paper')
    draw_grid(ydict)


def fold_paper(axis, position, xdict, ydict):
    """Given x or y axis and position to fold, return folded paper's coordinates (dict)."""
    axis_dict = xdict if axis == 'x' else ydict
    other_dict = ydict if axis == 'x' else xdict

    top = {y: axis_dict[y] for y in axis_dict.keys() if y in range(position)}
    # bottom = {y: axis_dict[y] for y in axis_dict.keys() if y not in range(position + 1)}
    calc_bottom = {y - abs(y - position) * 2: axis_dict[y] for y in axis_dict.keys() if y not in range(position + 1)}

    combined_keys = set(top.keys()) | set(calc_bottom.keys())  # use & or |?

    # dict comprehension to combine points in top or calc_bottom or both
    combined = {y: top.get(y, set()) | calc_bottom.get(y, set()) for y in combined_keys}

    print('top + calc_bottom of axis_dict = ')
    pprint(combined)

    if axis == 'x':
        return combined, update_other_dict(combined)
    return update_other_dict(combined), combined


def update_other_dict(new_dict):
    other_dict = {}

    for key, values in new_dict.items():
        # other_dict = {val: other_dict[val] | {key} for val in values}
        for value in values:
            if value not in other_dict:
                other_dict[value] = set()
            other_dict[value].add(key)

    print(f'* now, other_dict has been updated! *')
    pprint(other_dict)
    return other_dict


def count_points(adict):
    count = 0
    for key, values in adict.items():
        count += len(values)
    return count


def find_dimensions(ydict):
    max_x = max_y = 0
    for y, x_set in ydict.items():
        if y > max_y:
            max_y = y
        x = max(x_set)
        if x > max_x:
            max_x = x
    return max_x, max_y


def draw_grid(ydict):
    print('\nStarting to draw the grid now, using ydict below!\n')
    pprint(ydict)
    grid = []
    max_x, max_y = find_dimensions(ydict)
    for y in range(max_y + 1):
        x_set = ydict.get(y, None)
        if x_set is None:
            row_str = ' ' * (max_x + 1)
        else:
            row = ['#' if x in x_set else ' ' for x in range(max_x + 1)]
            row_str = ''.join(row)
        grid.append(row_str)
        print(row_str)
    print('')
    pprint(grid)
    return grid


def draw_grid_pd(ydict):
    d = {y: list(ydict[y]) for y in ydict.keys()}
    df = pd.DataFrame(d)
    # df.apply(lambda c: pd.Series(c.name, c.values)).fillna('-').T  # FIXME
    print(df)


if __name__ == '__main__':
    # file = 'test_inputs/test13.txt'
    file = 'inputs/input13.txt'

    x_keys, y_keys, instructions = initialize(file)
    run_program(x_keys, y_keys, instructions)
    draw_grid_pd(y_keys)
