"""Utility functions for Advent of Code 2021."""


def read_input(file, convert_to_int=False):
    text = []
    with open(file, 'r') as f:
        for line in f.readlines():
            text.append(int(line.strip())) if convert_to_int else text.append(line.strip())
    return text
