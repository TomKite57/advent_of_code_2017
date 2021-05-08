# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(' ') for line in file]


class computer:
    def __init__(self, commands, start_val=0):
        self.commands = commands
        self.registers = dict()
        self.sent = []
        self.recieved = []
        self.current_command = 0
        self.send_counter = 0

        # Initialise registers
        for line in commands:
            self.registers[line[1]] = start_val

    def get_val(self, val):
        try:
            return int(val)
        except ValueError:
            return self.registers[val]

    def can_run(self):
        return not (self.commands[self.current_command][0] == 'rcv' and len(self.recieved) == 0)

    def run_command(self, command):
        try:
            a, b, c = command
        except ValueError:
            a, b = command
            c = None

        if a == "set":
            self.registers[b] = self.get_val(c)

        elif a == "add":
            self.registers[b] += self.get_val(c)

        elif a == "mul":
            self.registers[b] *= self.get_val(c)

        elif a == "mod":
            self.registers[b] %= self.get_val(c)

        elif a == "snd":
            self.sent.append(self.get_val(b))
            self.send_counter += 1

        elif a == "jgz":
            if self.get_val(b) > 0:
                self.current_command += self.get_val(c) - 1

        elif a == "rcv":
            if len(self.recieved) == 0:
                return
            self.registers[b] = self.recieved.pop(0)

        self.current_command = (self.current_command + 1)%len(self.commands)

    def run_till_fail(self):
        while self.can_run():
            command = self.commands[self.current_command]
            self.run_command(command)


def run_duet(commands):
    comp0 = computer(commands, 0)
    comp1 = computer(commands, 1)
    while comp0.can_run() or comp1.can_run():
        comp0.run_till_fail()
        comp1.run_till_fail()
        comp0.recieved, comp1.recieved = comp1.sent, comp0.sent
        comp0.sent, comp1.sent = [], []
    return comp1.send_counter


def part1(filename):
    data = readfile(filename)
    my_comp = computer(data)
    my_comp.run_till_fail()
    print("Solution: {}.".format(my_comp.sent[-1]))


def part2(filename):
    data = readfile(filename)
    answer = run_duet(data)
    print("Solution: {}.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day18.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day18.dat")
    timer.checkpoint_hit()

    timer.end_hit()
