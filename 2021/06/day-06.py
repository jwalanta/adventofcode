#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/6
#

from collections import defaultdict

def read_input():
    f = open("input.txt")
    return [int(l) for l in f.readline().split(",")]

input = read_input()

def part1():
    fish = input.copy()
    for _ in range(80):
        new = 0
        for i in range(len(fish)):
            fish[i] = fish[i] - 1
            if fish[i] == -1:
                fish[i] = 6
                new = new + 1
        
        fish = fish + [8] * new

    return len(fish)


def part2():
    # naive part1() will take forever to finish

    f = defaultdict(int)
    for n in input: # bucket into age groups
        f[n] = f[n] + 1

    for i in range(256):
        ng = defaultdict(int)

        # generate new generation of age groups
        ng[0] = f[1]
        ng[1] = f[2]
        ng[2] = f[3]
        ng[3] = f[4]
        ng[4] = f[5]
        ng[5] = f[6]
        ng[6] = f[7] + f[0] # existing 0s turn into 6s
        ng[7] = f[8]
        ng[8] = f[0] # spawn

        f = ng

    return sum([f[i] for i in f])


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
