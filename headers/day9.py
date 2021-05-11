# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


class group:
    def __init__(self, stream, start_ind=0, score=0):
        self.contents = []
        self.garbage_count = 0
        self.end_ind = -1
        self.start_ind = start_ind
        self.score = score
        ind = start_ind

        while ind < len(stream):

            if stream[ind] == '{':
                self.contents.append(group(stream, ind+1, self.score + 1))
                ind = self.contents[-1].end_ind + 1
                continue
            if stream[ind] == '}':
                self.end_ind = ind
                return
            if stream[ind] == '<':
                ind += 1
                while stream[ind] != '>':
                    if stream[ind] == '!':
                        ind += 2
                        continue
                    ind += 1
                    self.garbage_count += 1
                ind += 1
                continue
            ind += 1

    def get_total_score(self):
        return sum([g.get_total_score() for g in self.contents]) + self.score

    def get_total_garbage(self):
        return sum([g.get_total_garbage() for g in self.contents]) + self.garbage_count


def part1(filename):
    data = readfile(filename)
    my_group = group(data)
    print("Solution: {}.".format(my_group.get_total_score()))


def part2(filename):
    data = readfile(filename)
    my_group = group(data)
    print("Solution: {}.".format(my_group.get_total_garbage()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day9.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day9.dat")
    timer.checkpoint_hit()

    timer.end_hit()
