# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


class turing_machine:
    def __init__(self):
        self.state = 'A'
        self.tape = dict()
        self.pos = 0
        self.evolutions = {'A': self.A_evolve,
                           'B': self.B_evolve,
                           'C': self.C_evolve,
                           'D': self.D_evolve,
                           'E': self.E_evolve,
                           'F': self.F_evolve}

    def evolve(self, iterations):
        for _ in range(iterations):
            self.evolutions[self.state]()

    def checksum(self):
        return len(self.tape.keys())

    def A_evolve(self):
        if not self.tape.get(self.pos, 0):
            self.tape[self.pos] = 1
            self.pos += 1
            self.state = 'B'
        else:
            self.tape.pop(self.pos)
            self.pos -= 1
            self.state = 'C'

    def B_evolve(self):
        if not self.tape.get(self.pos, 0):
            self.tape[self.pos] = 1
            self.pos -= 1
            self.state = 'A'
        else:
            self.pos += 1
            self.state = 'D'

    def C_evolve(self):
        if not self.tape.get(self.pos, 0):
            self.pos -= 1
            self.state = 'B'
        else:
            self.tape.pop(self.pos)
            self.pos -= 1
            self.state = 'E'

    def D_evolve(self):
        if not self.tape.get(self.pos, 0):
            self.tape[self.pos] = 1
            self.pos += 1
            self.state = 'A'
        else:
            self.tape.pop(self.pos)
            self.pos += 1
            self.state = 'B'

    def E_evolve(self):
        if not self.tape.get(self.pos, 0):
            self.tape[self.pos] = 1
            self.pos -= 1
            self.state = 'F'
        else:
            self.pos -= 1
            self.state = 'C'

    def F_evolve(self):
        if self.tape.get(self.pos, 0) == 0:
            self.tape[self.pos] = 1
            self.pos += 1
            self.state = 'D'
        else:
            self.pos += 1
            self.state = 'A'



def part1(filename):
    machine = turing_machine()
    machine.evolve(12481997)
    print("Solution: {}.".format(machine.checksum()))


def part2(filename):
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day25.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day25.dat")
    timer.checkpoint_hit()

    timer.end_hit()
