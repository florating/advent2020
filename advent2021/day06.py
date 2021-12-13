"""Day 6: Lanternfish"""

LIMIT = 7


def process_days(fishes, days=18):
    # print(f'Initial state: {fishes}')
    for i in range(days):
        babies = 0
        for j, fish in enumerate(fishes):
            if not fish:
                fishes[j] = LIMIT - 1  # 0-index
                babies += 1
                # print(f'Now babies = {babies} because fish = {fish} at j = {j}')
            else:
                fishes[j] -= 1
        fishes.extend([8] * babies)
        # print(f'After {i + 1} day: {fishes}') if i == 0 \
        #     else print(f'After {i + 1} days: {fishes}')
    return len(fishes)


def count_progeny(timer, days):
    """Count # direct progeny from a given fish with initial timer (in days) and total # days to progress."""
    if timer >= days:
        return 0
    progeny = 1
    later_time = days - (timer + 1)
    progeny += later_time // LIMIT
    count_progeny(8, later_time)
    return progeny


if __name__ == '__main__':
    file = 'test_inputs/test06.txt'
    # file = 'inputs/input06.txt'

    data = [int(x) for x in open(file, 'r').read().strip().split(',')]

    days = 18
    print(process_days([1], days))
