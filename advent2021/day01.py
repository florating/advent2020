"""Day 1: submarines, measurements, and sliding windows"""


from utils import read_input


def count_increases(data):
    """Count the # of times there is an increase when comparing consecutive measurement data.
    >>> test = 'test01.txt'
    >>> test_nums = read_input(test, convert_to_int=True)
    >>> count_increases(test_nums)
    7
    >>> test_sums = sum_measures(test_nums)
    >>> count_increases(test_sums)
    5
    """
    count = 0
    prev = data[0]
    for num in data[1:]:
        if num > prev:
            count += 1
        prev = num
    return count


def sum_measures(nums):
    """Calculate 3-measurement sliding windows using nums (list).
    EG: i = 0, 4, 8, ... all mark the index position for the start of the 3-measure window
    """
    sums = []
    i, j, k = 0, 1, 2
    while k < len(nums):
        sums.append(nums[i] + nums[j] + nums[k])
        i, j, k = j, k, k + 1
    return sums


if __name__ == '__main__':
    file = 'input01.txt'
    lst = read_input(file, convert_to_int=True)
    print(f'The answer to part 1 is: {count_increases(lst)}')

    sums = sum_measures(lst)
    print(f'The answer to part 2 is: {count_increases(sums)}')
