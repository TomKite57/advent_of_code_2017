# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [[x for x in line.strip('\n')] for line in file]


class cart:
    def __init__(self, map):
        self.map = map
        self.initialise_cart()
        self.letters = []
        self.movements = 0

    def initialise_cart(self):
        for i, tile in enumerate(self.map[0]):
            if tile == '|':
                self.pos = [i, 0]
                self.velocity = [0, 1]
                return

    def check_tile(self, x=None, y=None):
        if None in [x, y]:
            x, y = self.pos
        if 0 <= y < len(self.map) and 0 <= x < len(self.map[y]):
            return self.map[y][x]
        return ' '

    def advance(self):
        if not self.check_tile() in ['+', ' ']:
            self.pos[0] += self.velocity[0]
            self.pos[1] += self.velocity[1]
        else:
            if self.velocity[0] == 0 and self.check_tile(self.pos[0]+1, self.pos[1]) != ' ':
                self.velocity = [1, 0]
                self.pos[0] += 1
            elif self.velocity[0] == 0 and self.check_tile(self.pos[0]-1, self.pos[1]) != ' ':
                self.velocity = [-1, 0]
                self.pos[0] -= 1
            elif self.velocity[1] == 0 and self.check_tile(self.pos[0], self.pos[1]+1) != ' ':
                self.velocity = [0, 1]
                self.pos[1] += 1
            elif self.velocity[1] == 0 and self.check_tile(self.pos[0], self.pos[1]-1) != ' ':
                self.velocity = [0, -1]
                self.pos[1] -= 1
            else:
                return False

        if self.check_tile() not in ['|', '-', '+', ' ']:
            self.letters.append(self.check_tile())
        self.movements += 1
        return True

    def evolve_till_crash(self):
        while self.advance():
            pass

    def final_word(self):
        rval = ""
        for l in self.letters:
            rval += l
        return rval


def part1(filename):
    data = readfile(filename)
    my_cart = cart(data)
    my_cart.evolve_till_crash()
    print("Solution: {}.".format(my_cart.final_word()))


def part2(filename):
    data = readfile(filename)
    my_cart = cart(data)
    my_cart.evolve_till_crash()
    print("Solution: {}.".format(my_cart.movements))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day19.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day19.dat")
    timer.checkpoint_hit()

    timer.end_hit()
