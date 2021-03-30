# -*- coding: utf-8 -*-

from aoc_tools import Advent_Timer

cond_dict = {'==': lambda x, y: x==y,
             '!=': lambda x, y: x!=y,
             '<': lambda x, y: x<y,
             '<=': lambda x, y: x<=y,
             '>': lambda x, y: x>y,
             '>=': lambda x, y: x>=y}

sign_dict = {'inc': +1,
             'dec': -1}

def process_line(line):
    segs = line.strip().split(' ')
    segs[2] = int(segs[2])
    segs[6] = int(segs[6])
    return segs[:3] + segs[4:]


def readfile(filename):
    with open(filename, 'r') as file:
        return [process_line(line) for line in file]


def run_rules(rules):
    max_val = 0
    registers = dict([(line[0], 0) for line in rules])
    for line in rules:
        if cond_dict[line[4]](registers[line[3]], line[5]):
            registers[line[0]] += sign_dict[line[1]]*line[2]
        if registers[line[0]] > max_val:
            max_val = registers[line[0]]
    return registers, max_val


def part1(filename):
    data = readfile(filename)
    registers, _ = run_rules(data)
    print("Solution: {}.".format(max(registers.values())))


def part2(filename):
    data = readfile(filename)
    _, max_val = run_rules(data)
    print("Solution: {}.".format(max_val))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day8.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day8.dat")
    timer.checkpoint_hit()

    timer.end_hit()
