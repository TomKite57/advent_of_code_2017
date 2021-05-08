# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return int(file.read().strip())


def insert_in_array(array, val, pos):
    return array[:pos] + [val,] + array[pos:]


class spinlock:
    def __init__(self, step_size):
        self.array = [0,]
        self.current_pos = 0
        self.next_num = 1
        self.step_size = step_size
        self.p2_answer = 1
        self.array_len = 1

    def add_num(self, iterations=1):
        for _ in range(iterations):
            self.current_pos = (self.current_pos + self.step_size)%len(self.array) + 1
            self.array = insert_in_array(self.array, self.next_num, self.current_pos)
            self.next_num += 1

    def add_num_cheap(self, iterations=1):
        for _ in range(iterations):
            self.current_pos = (self.current_pos + self.step_size)%self.array_len + 1
            if self.current_pos == 1:
                self.p2_answer = self.next_num
            self.next_num += 1
            self.array_len += 1

    def p1_checksum(self):
        return self.array[(self.current_pos+1)%len(self.array)]

    def p2_checksum(self):
        return self.p2_answer

    def __str__(self):
        rval = ""
        for i, val in enumerate(self.array):
            if i == self.current_pos:
                rval += "({}) ".format(val)
            else:
                rval += "{} ".format(val)
        return rval


def part1(filename):
    data = readfile(filename)
    my_spinlock = spinlock(data)
    my_spinlock.add_num(2017)
    print("Solution: {}.".format(my_spinlock.p1_checksum()))


def part2(filename):
    data = readfile(filename)
    my_spinlock = spinlock(data)
    my_spinlock.add_num_cheap(50000000)
    print("Solution: {}.".format(my_spinlock.p2_checksum()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day17.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day17.dat")
    timer.checkpoint_hit()

    timer.end_hit()
