# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

START_PATTERN = '.#./..#/###'


def parse_line(line):
    return line.strip().split(' => ')


def readfile(filename):
    rval = dict()
    with open(filename, 'r') as file:
        data = [parse_line(line) for line in file]
    for line in data:
        rval[line[0]] = line[1]
    return rval


def line_to_grid(line):
    return [[y for y in x] for x in line.split('/')]


def grid_to_line(grid):
    rval = ''
    for line in grid:
        for char in line:
            rval += char
        rval += '/'
    return rval[:-1]


def subgrid(grid, coord, length):
    return [[grid[y][x] for x in range(coord[0], coord[0]+length)]
             for y in range(coord[1], coord[1]+length)]


def line_to_sections(line):
    grid = line_to_grid(line)
    if len(grid)%2 == 0:
        sec_num = len(grid)//2
        rval = [[] for _ in range(sec_num)]
        for i in range(0, sec_num):
            for j in range(0, sec_num):
                rval[i].append(grid_to_line(subgrid(grid, [2*j, 2*i], 2)))
        return rval

    if len(grid)%3 == 0:
        sec_num = len(grid)//3
        rval = [[] for _ in range(sec_num)]
        for i in range(0, sec_num):
            for j in range(0, sec_num):
                rval[i].append(grid_to_line(subgrid(grid, [3*j, 3*i], 3)))
        return rval

    raise Exception("Grid not divisible by 2 or 3!")


def sections_to_line(sections_arr):
    rval = ""
    slash_count = sections_arr[0][0].count('/') + 1
    for row in sections_arr:
        for i in range(slash_count):
            temp = ''
            for elem in row:
                temp += elem.split('/')[i]
            rval += temp + '/'
    return rval[:-1]


def flip_grid(grid):
    return [row[::-1] for row in grid]


def rotate_grid(grid):
    rval = [[[] for elem in row] for row in grid]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            rval[len(grid)-x-1][y] = grid[y][x]
    return rval


def evolve_section(section, rules):
    counter = 0
    while section not in rules:
        if counter > 8:
            raise Exception("Could not find valid permutation for {}".format(section))
        if counter == 3:
            section = grid_to_line(flip_grid(line_to_grid(section)))
        else:
            section = grid_to_line(rotate_grid(line_to_grid(section)))
        counter += 1
    return rules[section]


def evolve_n_times(line, rules, n=1):
    for _ in range(n):
        sections = line_to_sections(line)
        sections = [[evolve_section(sec, rules) for sec in row] for row in sections]
        line = sections_to_line(sections)
    return line


def show(line):
    print(line.replace('/', '\n'))


def part1(filename):
    data = readfile(filename)
    line = evolve_n_times(START_PATTERN, data, 5)
    print("Solution: {}.".format(line.count('#')))


def part2(filename):
    data = readfile(filename)
    line = evolve_n_times(START_PATTERN, data, 18)
    print("Solution: {}.".format(line.count('#')))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day21.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day21.dat")
    timer.checkpoint_hit()

    timer.end_hit()
