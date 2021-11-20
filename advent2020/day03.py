from day01 import read_input


def get_position(land, current, x, y):
    """Return the (x, y) coordinates of the next position when traveling to the right x and down y positions."""
    width = len(land[0])  # assume land map repeats horizontally ad infinitum, so just use a single row to calculate
    (xi, yi) = current
    xf = xi + x
    if xf >= width:
        xf -= width
    return xf, y + yi


def is_tree(land, coord):
    """Return True if the coord position is a tree (represented as #)."""
    x, y = coord
    return land[y][x] == '#'


def traverse(land, x=3, y=1):
    """Count and return the number of trees in the path when traversing the land map.
    >>> test = 'day03_test.txt'
    >>> traverse(read_input(test))
    7
    """
    yf = count = 0
    current = (0, 0)
    while yf < len(land) - 1:
        xf, yf = get_position(land, current, x, y)
        current = (xf, yf)
        if is_tree(land, current):
            count += 1
    return count


def main(is_p2=False):
    # test = 'day03_test.txt'
    filepath = 'day03_input'
    terrain = read_input(filepath)
    prod = 1
    prod *= traverse(terrain, 3, 1)
    if is_p2:
        prod *= traverse(terrain, 1, 1)
        prod *= traverse(terrain, 5, 1)
        prod *= traverse(terrain, 7, 1)
        prod *= traverse(terrain, 1, 2)
    return prod


if __name__ == "__main__":
    print(main())
    print(main(is_p2=True))
