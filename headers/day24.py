# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in line.split('/')] for line in file]


def valid_bridge(order, parts):
    bridge = [[0,0], ]
    for i in order:
        part = parts[i]
        if bridge[-1][1] == part[0]:
            bridge.append(part)
            continue
        if bridge[-1][1] == part[1]:
            bridge.append(part[::-1])
            continue
        return False
    return True


def find_next_part(bridge_ind, parts):
    rval = []
    final_piece = parts[bridge_ind[-1]]
    set_final_piece = set(final_piece)
    set_bridge_ind = set(bridge_ind)

    for i, part in enumerate(parts):
        if i in set_bridge_ind:
            continue
        #if final_piece[0] in part or final_piece[1] in part:
        if set_final_piece.intersection(part):
            test = bridge_ind + [i,]
            if valid_bridge(test, parts):
                rval.append(test)
            continue
    return rval


def get_combinations(parts):
    indices = list(range(len(parts)))
    current_bridge_ind = [[i,] for i in indices if 0 in parts[i]]
    all_bridge_ind = [] + current_bridge_ind
    for _ in range(len(parts)):
        next_round = []
        for i in range(len(current_bridge_ind)):
            next_round += find_next_part(current_bridge_ind[i], parts)

        if len(next_round) == 0:
            return all_bridge_ind
        current_bridge_ind = next_round
        all_bridge_ind += current_bridge_ind        


def bridge_strength(bridge_ind, parts):
    return sum([sum(parts[i]) for i in bridge_ind])


def part1(filename):
    data = readfile(filename)
    bridge_inds = get_combinations(data)
    max_bridge = max(bridge_inds, key=lambda x: bridge_strength(x, data))
    print("Solution: {}.".format(bridge_strength(max_bridge, data)))


def part2(filename):
    data = readfile(filename)
    bridge_inds = sorted(get_combinations(data), key=len, reverse=True)
    bridge_inds = [b for b in bridge_inds if len(b) == len(bridge_inds[0])]
    max_bridge = max(bridge_inds, key=lambda x: bridge_strength(x, data))
    print("Solution: {}.".format(bridge_strength(max_bridge, data)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day24.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day24.dat")
    timer.checkpoint_hit()

    timer.end_hit()
