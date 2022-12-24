"""Day 10: Cathode-Ray Tube"""

from utils import read_input

CYCLES = [20, 60, 100, 140, 180, 220]


class CPU:
    def __init__(self):
        self.cycles = 0
        self.x = 1
        self.signals = {}
        self.drawing = ''

    def parse(self, code_line):
        """Only increase cycle count for 'noop'."""
        self.tick()

        if code_line[:4] == 'addx':
            self.tick()
            self.x += int(code_line.strip().split()[-1])  # v

    def tick(self):
        self.cycles += 1
        self.draw()
        self.record_signal()

    def record_signal(self):
        self.signals[self.cycles] = self.x

    def get_signal(self, cycle_num):
        return self.signals[cycle_num]

    def calculate_signal_strength(self, cycle_num):
        return cycle_num * self.get_signal(cycle_num)

    def print_signal(self, cycle_num):
        print(f'cycle = {cycle_num}, X = {self.get_signal(cycle_num)}')

    def draw(self):
        position = self.cycles % 40 - 1
        if position == 0:
            self.drawing += '\n'
        if abs(position - self.x) <= 1:
            self.drawing += '#'
        else:
            self.drawing += '.'


def main(text):
    """
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    What is the sum of these six signal strengths?
    """
    cpu = CPU()

    # populate the signal strength dict
    for line in text:
        cpu.parse(line)

    ans = 0
    for val in CYCLES:
        curr = cpu.calculate_signal_strength(val)
        # print(f'cycle = {val}, signal strength = {curr}')
        ans += curr

    print(f'final cycle = {cpu.cycles}, final X = {cpu.x}')
    print(cpu.drawing)
    return ans


if __name__ == '__main__':
    program = read_input('inputs/10.txt')
    # program = read_input('test_inputs/10.txt')
    print(main(program))

"""
###..#....####.####.####.#.....##..#####
#..#.#....#.......#.#....#....#..#.#...#
#..#.#....###....#..###..#....#....###..
###..#....#.....#...#....#....#.##.#...#
#.#..#....#....#....#....#....#..#.#...#
#..#.####.####.####.#....####..###.####.

It's messing up the final position of each row somehow... at position 39

The answer is not 'RLEZFLGB'. The solution was 'RLEZFLGE'.
"""
