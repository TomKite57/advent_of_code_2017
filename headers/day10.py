# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().strip().split(',')]


def readfile_ascii(filename):
    with open(filename, 'r') as file:
        return [ord(x) for x in file.read().strip()]


def bitwise_xor(list_in):
    rval = 0
    for x in list_in:
        rval ^= x
    return rval


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


def part1(filename):
    data = readfile(filename)
    my_knot = knot(256, data)
    my_knot.run_rules()
    print("Solution: {}.".format(my_knot.get_checksum()))


def part2(filename):
    data = readfile_ascii(filename)
    my_knot = knot(256, data + [17, 31, 73, 47, 23])
    my_knot.run_rules(64)
    print("Solution: {}.".format(my_knot.get_hexadecimal()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day10.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day10.dat")
    timer.checkpoint_hit()

    timer.end_hit()
