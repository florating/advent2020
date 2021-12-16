"""Day 6: Lanternfish"""

LIMIT = 7


def process_days(fishes, days=18):
    print(f'Initial state: {fishes}')
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
        print(f'After {i + 1} day: {fishes}') if i == 0 \
            else print(f'After {i + 1} days: {fishes}')
    return len(fishes)


def count_fish(data, days):
    """Count # from a given fish with initial input and total # days to progress."""

    tracker = [data.count(i) for i in range(9)]
    print(f'Initial: {tracker}')
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
        # print(f'day {day + 1}: {tracker}')
    return sum(tracker)


if __name__ == '__main__':
    # file = 'test_inputs/test06.txt'
    file = 'inputs/input06.txt'

    data = [int(x) for x in open(file, 'r').read().strip().split(',')]

    days = 256
    # print(process_days(list([1]), days))

    print(count_fish(data, days))
