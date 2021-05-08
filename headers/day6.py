# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().strip().split('\t')]


class memory_bank:
    def __init__(self, initial_state):
        self.state = initial_state
        self.iterations = 0
        self.history = set()
        self.history.add(tuple(self.state))

    def evolve_step(self):
        index = min([i for i, val in enumerate(self.state)
                     if val == max(self.state)])
        blocks = self.state[index]
        self.state[index] = 0
        for i in range(blocks):
            self.state[(index+i+1)%len(self.state)] += 1
        self.iterations += 1

    def evolve_till_repeat(self):
        while True:
            self.evolve_step()
            temp_tup = tuple(self.state)
            if temp_tup in self.history:
                return
            self.history.add(temp_tup)



def part1(filename):
    data = readfile(filename)
    my_mem = memory_bank(data)
    my_mem.evolve_till_repeat()
    print("Solution: {}.".format(my_mem.iterations))


def part2(filename):
    data = readfile(filename)
    my_mem_1 = memory_bank(data)
    my_mem_1.evolve_till_repeat()
    my_mem_2 = memory_bank(my_mem_1.state)
    my_mem_2.evolve_till_repeat()
    print("Solution: {}.".format(my_mem_2.iterations))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day6.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day6.dat")
    timer.checkpoint_hit()

    timer.end_hit()
