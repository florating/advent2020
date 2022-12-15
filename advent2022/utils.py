"""Utility functions for Advent of Code 2022"""


def read_input(file, convert_to_int=False):
    text = []
    with open(file, 'r') as f:
        for line in f.readlines():
            next_line = int(line.strip()) if (convert_to_int and line not in {'', '\n'}) else line.strip()
            text.append(next_line)
    return text
