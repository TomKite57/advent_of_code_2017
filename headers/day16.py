# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def process_rule(line):
    if line[0] == 's':
        return ('s', int(line[1:]))
    x1, x2 = line[1:].split('/')
    if line[0] == 'x':
        return ('x', int(x1), int(x2))
    if line[0] == 'p':
        return ('p', x1, x2)
    raise Exception("Rule {} not recognised".format(line))


def readfile(filename):
    with open(filename, 'r') as file:
        return [process_rule(line) for line in file.read().strip().split(',')]


class dancers:
    def __init__(self, length=16):
        self.length = length
        self.dancers = dict()
        self.positions = dict()
        for x in range(length):
            self.dancers[chr(ord('a')+x)] = x
            self.positions[x] = chr(ord('a')+x)

    def gen_pos_from_dance(self):
        self.positions = dict()
        for dancer in self.dancers:
            self.positions[self.dancers[dancer]] = dancer

    def gen_dance_from_pos(self):
        self.dancers = dict()
        for pos in self.positions:
            self.dancers[self.positions[pos]] = pos

    def spin(self, dpos):
        for dancer in self.dancers:
            self.dancers[dancer] = (self.dancers[dancer] + dpos)%self.length
        self.gen_pos_from_dance()

    def exchange(self, pos_a, pos_b):
        self.positions[pos_a], self.positions[pos_b] = self.positions[pos_b], self.positions[pos_a]
        self.gen_dance_from_pos()

    def partner(self, dance_a, dance_b):
        self.dancers[dance_a], self.dancers[dance_b] = self.dancers[dance_b], self.dancers[dance_a]
        self.gen_pos_from_dance()

    def process_rule(self, rule):
        if rule[0] == 's':
            self.spin(int(rule[1]))
        elif rule[0] == 'x':
            self.exchange(rule[1], rule[2])
        elif rule[0] == 'p':
            self.partner(rule[1], rule[2])

    def full_dance(self, rules):
        for rule in rules:
            self.process_rule(rule)

    def get_order(self):
        rval = ""
        for x in range(self.length):
            rval += self.positions[x]
        return rval

    def show(self):
        print(*[self.positions[x] for x in range(self.length)])


def cyclic_dance(rules, iterations):
    my_dancers = dancers()
    states = dict()
    states[my_dancers.get_order()] = 0
    counter = 0
    while counter < iterations:
        my_dancers.full_dance(rules)
        counter += 1
        state = my_dancers.get_order()
        if state in states:
            loops, togo = divmod(iterations-counter, counter - states[state])
            for _ in range(togo):
                my_dancers.full_dance(rules)
            return my_dancers.get_order()
    return my_dancers.get_order()


def part1(filename):
    data = readfile(filename)
    my_dancers = dancers()
    my_dancers.full_dance(data)
    print("Solution: {}.".format(my_dancers.get_order()))


def part2(filename):
    data = readfile(filename)
    state = cyclic_dance(data, 1000000000)
    print("Solution: {}.".format(state))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day16.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day16.dat")
    timer.checkpoint_hit()

    timer.end_hit()
