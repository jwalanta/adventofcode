#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/5
#

from collections import defaultdict

input = []

def read_input():
    f = open("input.txt")
    for l in f.readlines():
        input.append(list(map(int, l.replace(" -> ", ",").strip().split(","))))

read_input()

def gen_range(n1, n2):
    return range(n2, n1 + 1) if n1 > n2 else range(n1, n2 + 1)

def part1():
    intersections = defaultdict(int)
    for c in input:
        x1, y1, x2, y2 = c
        if x1 == x2:
            for y in gen_range(y1, y2):
                intersections[(x1, y)] = intersections[(x1, y)] + 1
        
        if y1 == y2:
            for x in gen_range(x1, x2):
                intersections[(x, y1)] = intersections[(x, y1)] + 1

    return len([1 for k in intersections if intersections[k] > 1])


def part2():
    intersections = defaultdict(int)
    for c in input:
        x1, y1, x2, y2 = c

        if x1 == x2 or y1 == y2 or (abs(x1-x2) == abs(y1-y2)):
            dx = 0 if (x1 == x2) else (x2 - x1) / abs(x2 - x1)
            dy = 0 if (y1 == y2) else (y2 - y1) / abs(y2 - y1)
            x, y = x1, y1
            while x != x2 or y != y2:
                intersections[(x, y)] = intersections[(x, y)]  + 1
                x, y = x + dx, y + dy
            
            intersections[(x, y)] = intersections[(x, y)]  + 1

    return len([1 for k in intersections if intersections[k] > 1])


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())