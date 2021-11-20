def read_input(filepath='day01_input', conversion=None):
    """Parse a text file to generate and return a list of ints.
    >>> test_list = 'day01_test.txt'
    >>> read_input(test_list, conversion=int)
    [1721, 979, 366, 299, 675, 1456]
    """
    lst = []
    with open(filepath, mode='r') as f:
        for line in f.readlines():
            if conversion:
                lst.append(conversion(line.strip()))
            else:
                lst.append(line.strip())
    return lst


def sum_of_two(lst, target=2020):
    """Find the 2 entries that sum to 2020; return the product of those 2 values.
    >>> sum_of_two([1721, 979, 366, 299, 675, 1456])
    514579
    """
    seen = set()
    for num in lst:
        exp = target - num
        if exp in seen:
            # print(f'Great! {exp} + {num} = {target}')
            return exp * num
        else:
            seen.add(num)


def sum_of_three(lst):
    """Find the 3 entrees that sum to 2020; return the product of those 3 values.
    >>> sum_of_three([1721, 979, 366, 299, 675, 1456])
    241861950
    """
    for num in lst:
        exp = 2020 - num
        prod = sum_of_two([n for n in lst if n != num], exp)
        if prod:
            return prod * num


def main_p1():
    """Solve part 1 of day 1."""
    p1_list = read_input('day01_input', conversion=int)
    return sum_of_two(p1_list)


def main_p2():
    """Solve part 2 of day 1."""
    return sum_of_three(read_input('day01_input', conversion=int))


if __name__ == "__main__":
    print(main_p1())
    print(main_p2())
