# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer
from copy import deepcopy


def readfile(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(' ') for line in file]


class computer:
    def __init__(self, commands):
        self.commands = commands
        self.registers = dict()
        self.current_command = 0

        # Initialise registers
        for line in commands:
            try:
                self.registers[line[1]] = int(line[1])
            except ValueError:
                self.registers[line[1]] = 0
            try:
                self.registers[line[2]] = int(line[2])
            except ValueError:
                pass

        self.command_dict = {"set": self.set,
                             "mul": self.mul,
                             "sub": self.sub,
                             "jnz": self.jnz}

    def set(self, b, c):
        self.registers[b] = self.registers[c]
        self.current_command += 1

    def sub(self, b, c):
        self.registers[b] -= self.registers[c]
        self.current_command += 1

    def mul(self, b, c):
        self.registers[b] *= self.registers[c]
        self.current_command += 1

    def jnz(self, b, c):
        if self.registers[b]:
            self.current_command += self.registers[c]
        else:
            self.current_command += 1

    def run_till_fail(self):
        while True:
            try:
                c1, c2, c3 = self.commands[self.current_command]
                self.command_dict[c1](c2, c3)
            except IndexError:
                return

    def run_till_fail_count_mul(self):
        rval = 0
        while True:
            try:
                c1, c2, c3 = self.commands[self.current_command]
                self.command_dict[c1](c2, c3)
                if c1 == 'mul':
                    rval += 1
            except IndexError:
                return rval


def part1(filename):
    data = readfile(filename)
    my_comp = computer(data)
    mul_counter = my_comp.run_till_fail_count_mul()
    print("Solution: {}.".format(mul_counter))
    print("Solution: {}.".format(my_comp.registers['h']))


def part2(filename):
    return
    data = readfile(filename)
    my_comp = computer(data)
    my_comp.registers['a'] = 1
    my_comp.run_till_fail()
    print("Solution: {}.".format(my_comp.registers['h']))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day23.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day23.dat")
    timer.checkpoint_hit()

    timer.end_hit()



# b = 67*100 + 100000
# c = 67*100 + 117000
# f = 1
# d = 2
# e = 2
# g = 2
# g*e

# Loop continues till b-c == 0
