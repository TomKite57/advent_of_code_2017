# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [int(line.strip().split(" starts with ")[1]) for line in file]


def generator(start_val, factor, divisor, scrutiny=1):
    rval = start_val
    while True:
        rval = (rval*factor)%divisor
        if not rval%scrutiny:
            yield rval


def judge(numA, numB):
    return bin(numA)[2:].zfill(16)[-16:] == bin(numB)[2:].zfill(16)[-16:]


def part1(filename):
    data = readfile(filename)
    robotA = generator(data[0], 16807, 2147483647)
    robotB = generator(data[1], 48271, 2147483647)
    result = sum([judge(next(robotA), next(robotB)) for _ in range(40000000)])
    print("Solution: {}.".format(result))


def part2(filename):
    data = readfile(filename)
    robotA = generator(data[0], 16807, 2147483647, 4)
    robotB = generator(data[1], 48271, 2147483647, 8)
    result = sum([judge(next(robotA), next(robotB)) for _ in range(5000000)])
    print("Solution: {}.".format(result))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day15.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day15.dat")
    timer.checkpoint_hit()

    timer.end_hit()
