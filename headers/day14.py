# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer
from math import log2
import sys
sys.setrecursionlimit(5000)

def readfile(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def get_ascii_from_string(input):
    return [ord(x) for x in input]


def bitwise_xor(list_in):
    rval = 0
    for x in list_in:
        rval ^= x
    return rval


def hexa_to_bit(input):
    num_bits = len(input) * round(log2(16))
    return bin(int(input, 16))[2:].zfill(num_bits)


def dist(c1, c2):
    return abs( c2[0] - c1[0] ) + abs( c2[1] - c1[1] )
    #return sum([abs(c2[i]-c1[i]) for i in range(len(c1))])


def in_region(coord, reg):
    for elem in reg:
        if dist(coord, elem) < 2:
            return True
    return False


def joint_regions(reg1, reg2):
    for elem in reg1:
        if in_region(elem, reg2):
            return True
    return False


def simplify_regions(regions):
    changed = False
    i = 0
    while i < len(regions):
        dx = 1
        j = i+1
        while j < len(regions):
            dy = 1
            reg1 = regions[i]
            reg2 = regions[j]
            if joint_regions(reg1, reg2):
                regions[i] = set.union(reg1, reg2)
                regions.pop(j)
                changed = True
                dx = 0
                dy = 0
            j += dy
        i += dx
    return regions


class knot:
    def __init__(self, total_len, twist_lens):
        self.state = list(range(total_len))
        self.lengths = twist_lens
        self.current_pos = 0
        self.skip_size = 0

    def rotate_length(self, length):
        if length > len(self.state):
            raise Exception("Can't rotate more than length of list itself!")
        if self.current_pos + length >= len(self.state):
            to_rotate = self.state[self.current_pos:] + \
                        self.state[:(self.current_pos+length)%len(self.state)]
        else:
            to_rotate = self.state[self.current_pos:self.current_pos+length]

        to_rotate = to_rotate[::-1]

        for i in range(length):
            self.state[(self.current_pos+i)%len(self.state)] = to_rotate[i]

    def run_rules(self, num_repeats=1):
        if num_repeats == 0:
            return
        for length in self.lengths:
            self.rotate_length(length)
            self.current_pos = (self.current_pos + length + self.skip_size) % len(self.state)
            self.skip_size += 1
        self.run_rules(num_repeats-1)

    def get_checksum(self):
        return self.state[0] * self.state[1]

    def get_dense_hash(self):
        return [bitwise_xor(self.state[n:n+16]) for n in range(0,256,16)]

    def get_hexadecimal(self):
        dense_hash = self.get_dense_hash()
        rval = ''
        for hash in dense_hash:
            hexa = '00' + hex(hash)[2:]
            rval += hexa[-2:]
        return rval

    def get_defrag(self):
        return hexa_to_bit(self.get_hexadecimal())


class disk:
    def __init__(self, keyword):
        self.keyword = keyword
        self.grid = [[int(char) for char in self.get_row(i)] for i in range(128)]

    def get_row(self, row_num):
        temp_word = self.keyword + "-" + str(row_num)
        temp_knot = knot(256, get_ascii_from_string(temp_word) + [17, 31, 73, 47, 23])
        temp_knot.run_rules(64)
        return temp_knot.get_defrag()

    def count_total_used_space(self):
        return sum([sum(row) for row in self.grid])

    def count_regions(self):
        regions = []
        for i, row in enumerate(self.grid):
            for j, elem in enumerate(row):
                if not elem:
                    continue
                for reg in regions:
                    if in_region((j, i), reg):
                        reg.add((j, i))
                        break
                else:
                    regions.append(set([(j, i)]))
        return len(simplify_regions(regions))


def part1(filename):
    data = readfile(filename)
    my_disk = disk(data)
    print("Solution: {}.".format(my_disk.count_total_used_space()))


def part2(filename):
    data = readfile(filename)
    my_disk = disk(data)
    print("Solution: {}.".format(my_disk.count_regions()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day14.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day14.dat")
    timer.checkpoint_hit()

    timer.end_hit()
