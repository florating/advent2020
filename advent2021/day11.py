"""Day 11: Dumbo Octopus"""

from pprint import pprint


def get_input(file):
    """Return file input as a list of lists of ints (a matrix)."""
    data_grid = []
    with open(file, 'r') as f:
        for line in f.readlines():
            nums = map(int, list(line.strip()))
            data_grid.append(list(nums))
    return data_grid


def find_nearby_octos(coords, num_rows=10, num_cols=10):
    """Given coords (x, y), return a list/set of valid coords.
    >>> find_nearby_octos((1,1), 3, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    x, y = coords
    nearby = [
        (x - 1, y + i) for i in range(-1, 2, 1)
        if 0 <= y + i < num_rows and 0 <= x - 1 < num_cols
    ]
    nearby.extend([
        (x, y + i) for i in range(-1, 2, 2)
        if 0 <= y + i < num_rows
    ])
    nearby.extend([
        (x + 1, y + i) for i in range(-1, 2, 1)
        if (0 <= y + i < num_rows) and (0 <= x + 1 < num_cols)
    ])
    return nearby


def perform_actions(grid):
    """Count # of flashes for a single step that involves: increment energy, flash, and reset energy levels."""
    flashed = set()

    increment_grid(grid)
    flash(grid, flashed)
    count = len(flashed)
    # print(f'from within perform_actions: count = {count}')
    reset_levels(grid, flashed)
    return count


def increment_grid(grid):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            grid[y][x] += 1


def flash(grid, flashed):
    """Return # of flashes."""
    to_flash = []
    for y, row in enumerate(grid):
        to_flash.extend([
            (x, y) for x, val in enumerate(row) if val > 9
        ])
    incremented = {}
    # print(f'to_flash = {to_flash}')
    while to_flash:
        next_coord = to_flash.pop(0)
        # print(f'next_coord = {next_coord}')
        if next_coord not in flashed:
            flashed.add(next_coord)
            to_increment = find_nearby_octos(next_coord)
            # print(f'to_increment = {to_increment}')
            to_increment = [
                coord for coord in to_increment if coord not in flashed
            ]
            if to_increment:
                increment(grid, to_increment, incremented)
            can_flash = [coord for coord, value in incremented.items() if value > 9]
            to_flash.extend(can_flash)
    # print(f'flashed = {flashed}')
    return flashed


def increment(grid, coords, values_dict):
    for coord in coords:
        x, y = coord
        # print(f'x = {x} and y = {y}')
        grid[y][x] += 1
        values_dict[(x, y)] = grid[y][x]


def reset_levels(grid, flashed):
    for coord in flashed:
        x, y = coord
        # print(f'x = {x} and y = {y}')
        grid[y][x] = 0


def solve(grid, num_steps):
    count = 0
    for i in range(num_steps):
        count += perform_actions(grid)
    return count


def solve_p2(grid):
    steps = 0
    while True:
        count = perform_actions(grid)
        steps += 1
        if count == 100:
            return steps


if __name__ == '__main__':
    file = 'inputs/input11.txt'
    # file = 'test_inputs/test11.txt'

    grid = get_input(file)
    pprint(grid)

    ### for step 1:
    # steps = 100
    # count = solve(grid, steps)
    # print(f'After {steps} steps, # of flashes = {count}')
    # pprint(grid)

    step_all_flashed = solve_p2(grid)
    print(f'all flashed at step = {step_all_flashed}')
