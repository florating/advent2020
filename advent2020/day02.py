import re

from day01 import read_input


def parse_line(line, is_p1=True):
    """Parse line to be used as input for password validation.
    >>> parse_line('2-9 c: ccccccccc')
    {'password': 'ccccccccc', 'lo': 2, 'hi': 9, 'char': 'c'}
    >>> parse_line('1-3 a: abcde', is_p1=False)
    {'password': 'abcde', 'a': 0, 'b': 2, 'char': 'a'}
    """
    result = {}
    freq, char, result['password'] = line.split()
    a, b = map(int, freq.split('-'))
    if is_p1:
        result['lo'], result['hi'] = a, b
    else:
        result['a'], result['b'] = a - 1, b - 1  # switch to 0-index
    result['char'] = char[:-1]
    return result


def is_valid(lo, hi, char, password):
    """Return True if the password contains char at least lo times and at most hi times.
    >>> params = parse_line('2-9 c: ccccccccc')
    >>> is_valid(**params)
    True
    >>> params = parse_line('1-3 b: cdefg')
    >>> is_valid(**params)
    False
    """
    return lo <= len(re.findall(char, password)) <= hi


def is_valid_p2(a, b, char, password):
    """Return True if the password contains char in exactly one of these 1-indexed positions: a, b.
    >>> params = parse_line('2-9 c: ccccccccc', is_p1=False)
    >>> is_valid_p2(**params)
    False
    >>> params = parse_line('1-3 a: abcde', is_p1=False)
    >>> is_valid_p2(**params)
    True
    """
    return (password[a] == char) ^ (password[b] == char)


def main(filepath, is_p1=True):
    """Solve both parts 1 and 2 for day 2 (by changing is_p1 parameter).
    >>> test = 'day02_test.txt'
    >>> main(test)
    2
    >>> main(test, is_p1=False)
    1
    """
    count = 0
    validate = is_valid if is_p1 else is_valid_p2
    for line in read_input(filepath):
        if validate(**parse_line(line, is_p1=is_p1)):
            count += 1
    return count


if __name__ == "__main__":
    file = 'day02_input'
    print(main(file, is_p1=True))
    print(main(file, is_p1=False))  # for part 2
