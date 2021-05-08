# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in line.strip().split('\t')] for line in file]


def max_min_checksum(line):
    return max(line) - min(line)


def divisor_checksum(line):
    for i, val_a in enumerate(line):
        for val_b in line[i+1:]:
            if val_a % val_b == 0:
                return val_a // val_b
    raise Exception("No divisors found in divisor_checksum")


def part1(filename):
    data = readfile(filename)
    answer = sum([max_min_checksum(line) for line in data])
    print("Solution: {}.".format(answer))


def part2(filename):
    data = [sorted(line, reverse=True) for line in readfile(filename)]
    answer = sum([divisor_checksum(line) for line in data])
    print("Solution: {}.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day2.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day2.dat")
    timer.checkpoint_hit()

    timer.end_hit()
