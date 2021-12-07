#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/7
#

def read_input():
    f = open("input.txt")
    return [int(l) for l in f.readline().split(",")]

def find_min(distance_fn):
    min_total = None
    for p in range(min(input), max(input) + 1):
        total = 0
        for n in input:
            total = total + distance_fn(n, p)

        if min_total == None or total < min_total:
            min_total = total

    return min_total

def part1():
    return find_min(lambda x, y: abs(x - y))

def part2():
    return find_min(lambda x, y: sum(list(range(abs(x - y) + 1))))


input = read_input()

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
