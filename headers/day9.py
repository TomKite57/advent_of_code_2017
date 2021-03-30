# -*- coding: utf-8 -*-

from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return process_data(file.read().strip())


def process_data(data):
    # replace all unimportant chars
    print(data.count('!,'))
    all_chars = set(data)
    for char in all_chars:
        if char in ['{', '}', '<', '>', '!', ',']:
            continue
        data = data.replace(char, 'o')

    # remove everything after a !
    counter = 0
    while counter < len(data):
        if data[counter] == '!':
            data = data[:counter] + data[counter+2:]
            continue
        counter += 1
    return data

def part1(filename):
    data = readfile(filename)
    #print(data)
    #print("Solution: {}.".format())


def part2(filename):
    pass
    #data = readfile(filename)
    #print("Solution: {}.".format())


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day9.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day9.dat")
    timer.checkpoint_hit()

    timer.end_hit()
