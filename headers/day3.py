# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer
from math import ceil, floor, sqrt


def readfile(filename):
    with open(filename, 'r') as file:
        return int(file.read().strip())


def get_grid_coord(num):
    last_square = floor(sqrt(num))
    next_square = ceil(sqrt(num))
    if last_square == next_square:
        return next_square - 1
    if num == 1:
        return 0
    if (last_square % 2 == 0):
        # Bottom left corner
        if num == next_square**2:
            return next_square
        return min(abs(num - (next_square**2 - (last_square // 2))),
                   abs(num - (next_square**2 - 3*(last_square // 2)))) + last_square//2
    else:
        # Top right corner
        return min(abs(num - (last_square**2 + (next_square // 2))),
                   abs(num - (last_square**2 + 3*(next_square // 2)))) + next_square//2


def generate_grid_coords(upper_lim):
    direcs = [(1,0), (0,1), (-1,0), (0,-1)]
    coords = [(0,0),]
    run_length = 1
    counter = 1
    while counter <= upper_lim:
        x, y = direcs[0]
        for _ in range(run_length):
            coords.append((coords[-1][0] + x, coords[-1][1] + y))
        x, y = direcs[1]
        for _ in range(run_length):
            coords.append((coords[-1][0] + x, coords[-1][1] + y))
        x, y = direcs[2]
        for _ in range(run_length+1):
            coords.append((coords[-1][0] + x, coords[-1][1] + y))
        x, y = direcs[3]
        for _ in range(run_length+1):
            coords.append((coords[-1][0] + x, coords[-1][1] + y))
        run_length += 2
        counter += 4*run_length + 2
    return coords


def get_neighbours(coord):
    return [(coord[0]+dx, coord[1]+dy)
            for dx in [-1, 0, 1] for dy in [-1, 0, 1]
            if (dx!=0 or dy!=0)]

def populate_squares(coords, target):
    value_dict = {(0,0): 1,}
    for coord in coords:
        if coord == (0,0):
            continue
        value_dict[coord] = sum([value_dict.get(c, 0)
                                 for c in get_neighbours(coord)])
        if value_dict[coord] > target:
            return value_dict[coord]


def part1(filename):
    data = readfile(filename)
    print("Solution: {}.".format(get_grid_coord(data)))


def part2(filename):
    data = readfile(filename)
    coords = generate_grid_coords(data)
    print("Solution: {}.".format(populate_squares(coords, data)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day3.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day3.dat")
    timer.checkpoint_hit()

    timer.end_hit()
