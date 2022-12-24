"""Day 9: Rope Bridge"""

from utils import read_input
import math


class Knot:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.positions = {(self.row, self.col)}
        self.tail = None

    def set_tail(self, tail):
        self.tail = tail

    def move_once(self, code):
        if code == "U":
            self.row += 1
        elif code == "D":
            self.row -= 1
        elif code == "L":
            self.col -= 1
        elif code == "R":
            self.col += 1

    def move(self, instructions):
        """Move the head knot and its subsequent knot(s); records resulting change in position."""
        code, num = instructions.strip().split()
        for i in range(int(num)):
            self.move_once(code)
            curr = self
            while curr.tail is not None:
                curr.tail.update_tail_after_moving(curr)
                curr = curr.tail

    def get_coordinates(self):
        return self.col, self.row

    def update_tail_after_moving(self, head_knot):
        """From the perspective of the tail knot (aka self)."""
        # print(f'Head is at ({head_knot.col}, {head_knot.row}), aka [row={head_knot.row}][col={head_knot.col}]')
        delta_row = head_knot.row - self.row
        delta_col = head_knot.col - self.col

        euclidean_dist = math.dist(head_knot.get_coordinates(), self.get_coordinates())

        # knots_are_touching = True if abs(delta_row) <= 1 and abs(delta_col) <= 1 else False
        knots_are_touching = True if euclidean_dist <= 1.42 else False

        if not knots_are_touching:
            if euclidean_dist == 2:
                if abs(delta_col) == 2:
                    self.col += delta_col // 2
                else:
                    self.row += delta_row // 2

            else:
                self.col += delta_col if abs(delta_col) == 1 else delta_col // 2
                self.row += delta_row if abs(delta_row) == 1 else delta_row // 2
        # print(f'Tail is at ({self.col}, {self.row}), aka [row={self.row}][col={self.col}]\n')
        self.positions.add((self.row, self.col))
        return self.row, self.col


def main(text):
    head, tail = generate_multiple_knots(2)

    for line in text:
        head.move(line)
    return len(head.tail.positions)


def generate_multiple_knots(num=10):
    knots = []
    j = 0
    for i in range(num):
        knots.append(Knot())
        while j < i:
            knots[j].set_tail(knots[i])
            j += 1
    return knots


def main_p2(text):
    knots = generate_multiple_knots()

    for line in text:
        knots[0].move(line)
    return len(knots[-1].positions)


if __name__ == '__main__':
    instructions = read_input('inputs/09.txt')
    print(main(instructions))
    print(main_p2(instructions))
