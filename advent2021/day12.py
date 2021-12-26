"""Day 12: Passage Pathing"""

from pprint import pprint


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


def create_graph(lines):
    """
    >>> test_graph = create_graph(read_input('test_inputs/test12.txt'))
    >>> sorted(list(test_graph.keys()))
    ['A', 'b', 'start']
    """
    graph = {}
    for line in lines:
        start, end = line.strip().split('-')
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append(end)
        graph[end].append(start)
    return graph


def read_input(filepath):
    lines = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            lines.append(line)
    return lines


def traverse(gdict, starting_point='start'):
    visited = set()
    to_visit = gdict[starting_point]
    eligible_paths = gdict.copy()
    current_path = [starting_point]
    count = 0

    while to_visit:
        current = to_visit.pop(0)
        if current == 'end':
            current_path.append(current)
            count += 1
        elif current.islower():
            if current in visited:
                continue
            else:
                current_path.append(current)
                visited.add(current)
                to_visit.extend(eligible_paths[current])
                # del eligible_paths[current]
        else:
            current_path.append(current)
            to_visit.extend(eligible_paths[current])
    return count


if __name__ == '__main__':
    file = 'test_inputs/test12.txt'
    data = read_input(file)
    g = create_graph(data)
    pprint(g)
    path = traverse(g)
    print(path)
