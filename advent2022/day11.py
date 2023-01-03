"""Day 11: Monkey in the Middle"""

from collections import deque


class Monkey:
    def __init__(self):
        self.items = []
        self.test_val = None

    def parse(self):
        pass

    def test(self, val):
        return True if val % self.test_val == 0 else False

"""
Use a 2D array to get the structure.

[ m0, m1, m2, ... ]

Each monkey is an array of items to be handled.

eg: m0 = [ 79, 98 ]


"""

# could have used an array...
# [] = [if divisible by this value, true, false]
TEST = {
    0: [23, 2, 3],
    1: [19, 2, 0],
    2: [13, 1, 3],
    3: [17, 0, 1],
}


def main(text):
    for items in text['monkeys']:
        # process each monkey's list of items
        while items:
            val = items.popleft()

            # investigate
            operation = text['operations']

            # relief
            val = round(val / 3)

            # test
            test_criteria = text['tests']
            next_monkey = test_criteria[1] if val % test_criteria[0] == 0 else test_criteria[2]
            text['monkeys'][next_monkey].append(val)
            # if list is empty, the turn ends

    pass


def parse(text):
    monkeys, operations, tests = [], [], []
    with open(text) as f:
        for line in f:
            clean_line = line.strip()
            if clean_line == '':
                continue
            elif 'Start' in clean_line:
                vals = clean_line.split(':')[-1].strip().split(', ')
                monkeys.append(deque(map(int, vals)))
            elif 'Operation' in clean_line:
                operations.append(clean_line.split(':')[-1].strip())
            elif 'Test' in clean_line:
                test_case = [clean_line.split('y')[-1].split()[-1]]
                # if true:
                test_case.append(next(f).strip()[-1])
                # if false:
                test_case.append(next(f).strip()[-1])
                tests.append(list(map(int, test_case)))
    return {
        'monkeys': monkeys,
        'operations': operations,
        'tests': tests,
    }


if __name__ == '__main__':
    values_dict = parse('test_inputs/11.txt')
    print(values_dict)
    # main()
