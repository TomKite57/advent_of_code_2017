# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer
import sys
sys.setrecursionlimit(5000)

def process_line(line):
    line_a, line_b = line.strip().split(' <-> ')
    #return [int(line_a)] + [int(x) for x in line_b.split(', ')]
    return [int(x) for x in line_b.split(', ')]


def readfile(filename):
    with open(filename, 'r') as file:
        return [process_line(line) for line in file]


def create_initial_network(pipes):
    rval = []
    for index, connections in enumerate(pipes):
        all_indices = set([index, *connections])
        group_found = False
        for i, group in enumerate(rval):
            if bool(all_indices.intersection(group)):
                rval[i] = group.union(all_indices)
                group_found = True
                break
        if not group_found:
            rval.append(all_indices)
    return rval


def collect_groups(pipes, groups=None):
    if groups is None:
        groups = [set([i, *j]) for i, j in enumerate(pipes)]

    for i, g_i in enumerate(groups):
        for j, g_j in enumerate(groups[i+1:]):
            if bool(g_i.intersection(g_j)):
                groups[i] = g_i.union(g_j)
                return collect_groups(pipes, [g for k, g in enumerate(groups) if k != i+j+1])
    return groups


def part1(filename):
    data = readfile(filename)
    groups = collect_groups(data, create_initial_network(data))
    answer = [len(g) for g in groups if 0 in g][0]
    print("Solution: {}.".format(answer))


def part2(filename):
    data = readfile(filename)
    groups = collect_groups(data, create_initial_network(data))
    answer = len(groups)
    print("Solution: {}.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day12.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day12.dat")
    timer.checkpoint_hit()

    timer.end_hit()
