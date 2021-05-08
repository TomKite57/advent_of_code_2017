# -*- coding: utf-8 -*-

# pip install aoc-tools-dannyboywoop
from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        return [[x for x in line.strip().split(' ')] for line in file]


def repeated_word(passphrase):
    return len(passphrase) != len(set(passphrase))


def are_anagrams(word1, word2):
    if set(word1) != set(word2):
        return False
    for letter in set(word1):
        if word1.count(letter) != word2.count(letter):
            return False
    return True


def anagram_in_passphrase(passphrase):
    if repeated_word(passphrase):
        return True
    for i, word1 in enumerate(passphrase):
        for word2 in passphrase[i+1:]:
            if are_anagrams(word1, word2):
                return True
    return False


def part1(filename):
    data = readfile(filename)
    answer = sum(1 for line in data if not repeated_word(line))
    print("Solution: {}.".format(answer))


def part2(filename):
    data = readfile(filename)
    answer = sum(1 for line in data if not anagram_in_passphrase(line))
    print("Solution: {}.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day4.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day4.dat")
    timer.checkpoint_hit()

    timer.end_hit()
