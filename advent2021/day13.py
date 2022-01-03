"""Day 13: Transparent Origami"""


def initialize(filepath):
    x_to_y = {}  # keys = x-values; paired values = y-values with dots
    y_to_x = {}
    is_initialized = False
    folds = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()

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

            if not line:
                is_initialized = True

    return x_to_y, y_to_x, folds


def fold_paper(folds):
    for fold in folds:
        axis, num = fold
        pass
    # TODO


if __name__ == '__main__':
    file = 'test_inputs/test13.txt'
    # file = 'inputs/input13.txt'

    x_keys, y_keys, instructions = initialize(file)
