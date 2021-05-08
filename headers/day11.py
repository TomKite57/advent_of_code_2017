# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

pairs = [('n', 's'), ('ne', 'sw'), ('nw', 'se')]
maps = [
        [('sw', 'n'), 'nw'],
        [('se', 'n'), 'ne'],
        [('ne', 'nw'), 'n'],
        [('ne', 's'), 'se'],
        [('nw', 's'), 'sw'],
        [('se', 'sw'), 's'],
        ]
compatible_pairs = [set(('n', 'ne')),
                    set(('n', 'nw')),
                    set(('s', 'se')),
                    set(('s', 'sw')),
                    set(('nw', 'sw')),
                    set(('ne', 'se'))]


def readfile(filename):
    with open(filename, 'r') as file:
        return [x for x in file.read().strip().split(',')]


def remove_redundant_moves(path):
    to_remove = dict([(x, path.count(x)) for x in set(path)])
    for pair in pairs:
        val = min(to_remove.get(pair[0], 0), to_remove.get(pair[1], 0))
        to_remove[pair[0]] = val
        to_remove[pair[1]] = val

    counter = 0
    while sum(to_remove.values()) != 0:
        elem = path[counter]
        if to_remove[elem] != 0:
            del path[counter]
            to_remove[elem] -= 1
            continue
        counter += 1
    return path


def swap_moves(path, map_rule):
    to_remove = dict([(x, path.count(x)) for x in map_rule[0]])
    val = min([to_remove.get(x, 0) for x in map_rule[0]])
    for x in map_rule[0]:
        to_remove[x] = val

    counter = 0
    while sum(to_remove.values()) != 0:
        elem = path[counter]
        if to_remove.get(elem, 0) != 0:
            del path[counter]
            to_remove[elem] -= 1
            if elem == map_rule[0][0]:
                path.append(map_rule[1])
            continue
        counter += 1
    return path


def get_path_dist(path):
    path = remove_redundant_moves(path)
    for map in maps:
        path = swap_moves(path, map)
        path = remove_redundant_moves(path)
        set_path = set(path)
        if len(set_path) < 2 or set_path in compatible_pairs:
            return len(path)


def get_key_points(path):
    rval = []
    for i in range(len(path)-1):
        if path[i] != path[i+1]:
            rval.append(i)
    return rval


def alternative_dist(filename):
    #https://www.reddit.com/r/adventofcode/comments/7izym2/2017_day_11_solutions/
    #https://www.redblobgames.com/grids/hexagons/
    path = readfile(filename)
    x = 0
    y = 0
    z = 0
    dists = []
    for elem in path:
        if elem == "n":
            y += 1
            z -= 1
        elif elem == "s":
            y -= 1
            z += 1
        elif elem == "ne":
            x += 1
            z -= 1
        elif elem == "sw":
            x -= 1
            z += 1
        elif elem == "nw":
            x -= 1
            y += 1
        elif elem == "se":
            x += 1
            y -= 1
        dists.append((abs(x) + abs(y) + abs(z)) // 2)
    print("Solution: {}.".format(dists[-1]))
    print("Solution: {}.".format(max(dists)))


def part1(filename):
    data = readfile(filename)
    print("Solution: {}.".format(get_path_dist(data)))


def part2(filename):
    data = readfile(filename)
    max_dist = max([get_path_dist(data[:n]) for n in get_key_points(data)])
    print("Solution: {}.".format(max_dist))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day11.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day11.dat")
    timer.checkpoint_hit()

    print("Alternative_method:")
    alternative_dist("../data/day11.dat")
    timer.checkpoint_hit()

    timer.end_hit()


"""
Solution: 812.
Checkpoint time: 0.0127 seconds.


Part 2:
Solution: 1603.
Checkpoint time: 23.5577 seconds.
"""
