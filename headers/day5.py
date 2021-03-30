# -*- coding: utf-8 -*-

from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]


class jump_program:
    def __init__(self, code_in, offset_func_in=lambda x: 1):
        self.code = code_in
        self.current_pos = 0
        self.total_steps = 0
        self.offset_func = offset_func_in

    def jump(self):
        step = self.code[self.current_pos]
        self.code[self.current_pos] += self.offset_func(self.code[self.current_pos])
        self.current_pos += step
        self.total_steps += 1

    def jump_till_exit(self):
        while 0 <= self.current_pos < len(self.code):
            self.jump()


def part1(filename):
    data = readfile(filename)
    computer = jump_program(data)
    computer.jump_till_exit()
    print("Solution: {}.".format(computer.total_steps))


def part2(filename):
    data = readfile(filename)
    computer = jump_program(data, lambda x: 1 if x < 3 else -1)
    computer.jump_till_exit()
    print("Solution: {}.".format(computer.total_steps))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day5.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day5.dat")
    timer.checkpoint_hit()

    timer.end_hit()
