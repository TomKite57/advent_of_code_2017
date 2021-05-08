# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer


def parse_line(line):
    rval = []
    sublines = line.strip().split('>,')
    for sub in sublines:
        rval += [int(x) for x in sub.split('<')[1].strip('>').split(',')]
    return rval


def readfile(filename):
    with open(filename, 'r') as file:
        return [parse_line(line) for line in file]


def abs_sum(arr):
    return sum([abs(x) for x in arr])


def manhat_dist(arr1, arr2):
    return abs_sum([arr1[i] - arr2[i] for i in range(len(arr1))])


class particle:
    def __init__(self, properties, index=None):
        self.p0 = [properties[i] for i in [0,1,2]]
        self.v0 = [properties[i] for i in [3,4,5]]
        self.a0 = [properties[i] for i in [6,7,8]]
        self.index = index
        self.collided = 0

    def get_position(self, time=0):
        return [self.p0[i] + self.v0[i]*time + self.a0[i]*time*(time+1)/2 for i in [0,1,2]]

    def get_velocity(self, time=0):
        return [self.v0[i] + self.a0[i]*time for i in [0,1,2]]

    def get_acceleration(self, time=0):
        return self.a0

    def turn_time(self):
        return sum([-self.v0[i]/self.a0[i] for i in [0,1,2] if self.a0[i] != 0])

    def full_turn_time(self):
        time = self.turn_time()
        while self.dist(time) > self.dist(time+1):
            time += 1
        return time

    def dist(self, time, origin=[0,0,0]):
        return manhat_dist(self.get_position(time), origin)


    def get_properties(self):
        return [*self.p0, *self.v0, *self.a0]

    def __lt__(self, other):
        if abs_sum(self.a0) != abs_sum(other.a0):
            return abs_sum(self.a0) < abs_sum(other.a0)
        return self.dist(self.full_turn_time()) < other.dist(other.full_turn_time())

    def __gt__(self, other):
        if abs_sum(self.a0) != abs_sum(other.a0):
            return abs_sum(self.a0) > abs_sum(other.a0)
        return self.dist(self.full_turn_time()) > other.dist(other.full_turn_time())

    def __str__(self):
        rval = ""
        for x in (*self.p0, *self.v0, *self.a0):
            rval += str(x) + "\t"
        return rval


def get_max_time(all_particles):
    all_pairs = []
    for i, p1 in enumerate(all_particles):
        for j, p2 in enumerate(all_particles[i+1:]):
            all_pairs.append([b-a for a,b in zip(p1.get_properties(), p2.get_properties())])
    return max([particle(props).full_turn_time() for props in all_pairs])


def detect_collisions(particles):
    max_time = round(get_max_time(particles))
    for time in range(max_time):
        for i in range(len(particles)):
            if particles[i].collided:
                continue
            for j in range(i+1, len(particles)):
                if particles[j].collided:
                    continue
                if not manhat_dist(particles[i].get_position(time), particles[j].get_position(time)):
                    particles[i].collided = 1
                    particles[j].collided = 1
    return sum([1 for p in particles if not p.collided])


def part1(filename):
    data = readfile(filename)
    particles = sorted([particle(line, i) for i, line in enumerate(data)])
    print("Solution: {}.".format(particles[0].index))


def part2(filename):
    data = readfile(filename)
    particles = sorted([particle(line, i) for i, line in enumerate(data)])
    print("Solution: {}.".format(detect_collisions(particles)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day20.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day20.dat")
    timer.checkpoint_hit()

    timer.end_hit()
