"""Day 7: The Treachery of Whales"""


import math
import statistics


def find_meetup(nums):
    lo = meetup = None
    modes = statistics.multimode(nums)
    sd = math.ceil(statistics.pstdev(nums))
    print(f'modes = {modes}')
    print(f'sd = {sd}')

    values = set()
    for mode in modes:
        for i in range(sd):
            values.update({abs(mode + i), abs(mode - i)})

    for value in values:
        total_fuel = 0
        for position in nums:
            total_fuel += calculate_fuel(position, value)
        if not lo or total_fuel < lo:
            lo = total_fuel
            meetup = value
    return lo, meetup


def calculate_fuel(origin, target):
    """Calculate arithmetic sum:
    sum(a + kd) = n/2(2a + (n - 1)d)
    """
    n = abs(target - origin)
    a = d = 1
    total = (n / 2) * (2 * a + (n - 1) * d)
    return int(total)


if __name__ == '__main__':
    file = 'inputs/input07.txt'
    # file = 'test_inputs/test07.txt'

    data = open(file, 'r').readline().strip().split(',')
    positions = list(map(int, data))

    fuel, meetup_spot = find_meetup(positions)
    print(f'Use {fuel} fuel to get to meetup_spot = {meetup_spot}')
