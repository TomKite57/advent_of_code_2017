# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in line.split(':')] for line in file]


def guard_pos(time, guard_length):
    return time % (2*(guard_length-1))


def p1_checksum(guards):
    return sum([g[0]*g[1] for g in guards
                if not guard_pos(g[0], g[1])])


def is_time_valid(time, guards):
    for g in guards:
        if not guard_pos(time + g[0], g[1]):
            return False
    return True


def find_delay_time(guards):
    time = 0
    while True:
        if is_time_valid(time, guards):
            return time
        time += 1


def part1(filename):
    data = readfile(filename)
    print("Solution: {}.".format(p1_checksum(data)))


def part2(filename):
    data = readfile(filename)
    data = sorted(data, key=lambda x: x[1])
    print("Solution: {}.".format(find_delay_time(data)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day13.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day13.dat")
    timer.checkpoint_hit()

    timer.end_hit()
