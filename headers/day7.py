# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def process_line(line):
    segs = line.strip().split(' ')
    segs[1] = int(segs[1][1:-1])
    if len(segs) == 2:
        return segs
    return segs[:2] + [seg.strip(',') for seg in segs[3:]]


def readfile(filename):
    with open(filename, 'r') as file:
        return [process_line(line) for line in file]


def find_root(tree, current_node=None):
    if current_node is None:
        current_node = tree[0][0]

    for line in tree:
        if current_node in line[2:]:
            return find_root(tree, line[0])
    return current_node


def get_node_line(tree, node):
    return [x for x in tree if x[0] == node][0]


def get_line_containing_node(tree, node):
    return [x for x in tree if node in x[2:]][0]


def get_node_children(tree, node):
    return get_node_line(tree, node)[2:]


def get_node_weight(tree, node):
    return get_node_line(tree, node)[1]


def get_total_node_weight(tree, node):
    return get_node_weight(tree, node) + \
           sum([get_total_node_weight(tree, child)
                for child in get_node_children(tree, node)])


def valid_children(tree, node):
    weights = [get_total_node_weight(tree, child)
               for child in get_node_children(tree, node)]
    if len(weights) == 0:
        return True
    return len(set(weights)) == 1


def all_valid_children(tree, node):
    if not valid_children(tree, node):
        return False
    return all(all_valid_children(tree, child) for child in get_node_children(tree, node))


def find_bad_node(tree, node=None):
    if node is None:
        node = find_root(tree)
    if all_valid_children(tree, node):
        if node == find_root(tree):
            return None
        return node

    children = get_node_children(tree, node)
    weights = [get_total_node_weight(tree, child) for child in children]
    outlier = min(children, key = lambda c: weights.count(get_total_node_weight(tree, c)))
    return find_bad_node(tree, outlier)


def weight_needed(tree):
    problem_child = find_bad_node(tree)
    line = get_line_containing_node(tree, problem_child)
    twin = [x for x in line[2:] if x != problem_child][0]
    return abs(get_total_node_weight(tree, twin) - \
               get_total_node_weight(tree, problem_child) + \
               get_node_weight(tree, problem_child))


def part1(filename):
    data = readfile(filename)
    print("Solution: {}.".format(find_root(data)))


def part2(filename):
    data = readfile(filename)
    print("Solution: {}.".format(weight_needed(data)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day7.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day7.dat")
    timer.checkpoint_hit()

    timer.end_hit()
