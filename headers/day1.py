# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read()]


def part1(filename):
    data = readfile(filename)
    answer = sum([data[i] for i in range(len(data))
                  if data[i] == data[i-1]])
    print("Solution: {}.".format(answer))


def part2(filename):
    data = readfile(filename)
    answer = sum([data[i] for i in range(len(data))
                  if data[i] == data[i-len(data)//2]])
    print("Solution: {}.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day1.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day1.dat")
    timer.checkpoint_hit()

    timer.end_hit()
