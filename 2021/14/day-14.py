#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/14
#

from collections import Counter


def read_input():
    pairs = {}
    polymer = ""
    f = open("input.txt")
    for l in f.readlines():
        if "->" in l:
            k, v = l.strip().split(" -> ")
            pairs[k] = v
        elif l.strip() != "":
            polymer = l.strip()

    return polymer, pairs


def part1(polymer, pairs, steps):
    for _ in range(steps):
        c = Counter(polymer)

        new_polymer = ""
        for i in range(len(polymer)-1):
            k = polymer[i:i+2]
            if k in pairs:
                new_polymer = new_polymer + k[0] + pairs[k]
            else:
                new_polymer = new_polymer + k[0]
        new_polymer = new_polymer + polymer[-1]
        polymer = new_polymer

    c = Counter(polymer)
    return max(c.values()) - min(c.values())


def part2(polymer, pairs, steps):
    pairs_count = Counter()
    letters_count = Counter(polymer)

    # initialize
    for i in range(len(polymer)-1):
        pairs_count[polymer[i:i+2]] += 1

    for _ in range(steps):
        new_pairs_count = Counter()
        for k, v in pairs_count.items():
            ins = pairs[k]
            l, r = k
            new_pairs_count[l + ins] += v
            new_pairs_count[ins + r] += v
            letters_count[ins] += v

        pairs_count = new_pairs_count

    return max(letters_count.values()) - min(letters_count.values())


polymer, pairs = read_input()
print("Part 1: %d" % part1(polymer, pairs, 10))
print("Part 2: %d" % part2(polymer, pairs, 40))
