"""Day 6: Tuning Trouble"""


def solve(text, num_unique=4):
    pos = num_unique
    while pos < len(text):
        if len(set(text[pos - num_unique:pos])) == num_unique:
            return pos
        pos += 1


if __name__ == '__main__':
    ex1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    ex2 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    print(solve(ex2))

    with open('inputs/06.txt') as f:
        text = f.readline().strip()
        print(solve(text))
        print(solve(text, num_unique=14))
