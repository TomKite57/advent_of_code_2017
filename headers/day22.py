# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


class varus:
    def __init__(self, map_in):
        self.infected_tiles = set()
        for y in range(len(map_in)):
            for x in range(len(map_in[y])):
                if map_in[y][x] == '#':
                    self.infected_tiles.add( (x, y) )
        self.pos = [len(map_in[0])//2, len(map_in)//2]
        self.direc = [0, -1]
        self.infections = 0

    def move(self, iterations=1):
        for _ in range(iterations):
            tup_pos = tuple(self.pos)
            if tup_pos in self.infected_tiles:
                self.infected_tiles.remove(tup_pos)
                self.direc = [-self.direc[1], self.direc[0]]
            else:
                self.infected_tiles.add(tup_pos)
                self.direc = [self.direc[1], -self.direc[0]]
                self.infections += 1
            self.pos = [self.pos[0] + self.direc[0], self.pos[1] + self.direc[1]]

    def personal_infections(self):
        return self.infections


class varus_evolved:
    def __init__(self, map_in):
        self.weakened = set()
        self.infected = set()
        self.flagged = set()
        for y in range(len(map_in)):
            for x in range(len(map_in[y])):
                if map_in[y][x] == '#':
                    self.infected.add( (x, y) )
        self.pos = [len(map_in[0])//2, len(map_in)//2]
        self.direc = [0, -1]
        self.infections = 0

    def move(self, iterations=1):
        for _ in range(iterations):
            tup_pos = tuple(self.pos)
            if tup_pos in self.weakened:
                self.weakened.remove(tup_pos)
                self.infected.add(tup_pos)
                self.infections += 1
            elif tup_pos in self.infected:
                self.infected.remove(tup_pos)
                self.flagged.add(tup_pos)
                self.direc = [-self.direc[1], self.direc[0]]
            elif tup_pos in self.flagged:
                self.flagged.remove(tup_pos)
                self.direc = [-self.direc[0], -self.direc[1]]
            else:
                self.weakened.add(tup_pos)
                self.direc = [self.direc[1], -self.direc[0]]
            self.pos = [self.pos[0] + self.direc[0], self.pos[1] + self.direc[1]]

    def personal_infections(self):
        return self.infections


def part1(filename):
    data = readfile(filename)
    my_varus = varus(data)
    my_varus.move(10000)
    print("Solution: {}.".format(my_varus.personal_infections()))


def part2(filename):
    data = readfile(filename)
    my_varus = varus_evolved(data)
    my_varus.move(10000000)
    print("Solution: {}.".format(my_varus.personal_infections()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day22.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day22.dat")
    timer.checkpoint_hit()

    timer.end_hit()
