#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/9
#

def read_input():
    f = open("input.txt")
    return [l.strip() for l in f.readlines()]


def g(x, y):
    if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input):
        return 10
    return int(input[y][x])


def part1():
    sum = 0
    for x in range(len(input[0])):
        for y in range(len(input)):
            v = g(x, y)
            if v < g(x+1, y) and v < g(x-1, y) and v < g(x, y+1) and v < g(x, y-1):
                sum = sum + 1 + v
    return sum


def find_basin(x, y):
    if g(x, y) >= 9:
        return []

    basin = [(x, y)]

    if g(x, y) < g(x+1, y):
        basin = basin + find_basin(x+1, y)
    if g(x, y) < g(x-1, y):
        basin = basin + find_basin(x-1, y)
    if g(x, y) < g(x, y+1):
        basin = basin + find_basin(x, y+1)
    if g(x, y) < g(x, y-1):
        basin = basin + find_basin(x, y-1)

    return basin


def part2():
    basin_sizes = []
    for x in range(len(input[0])):
        for y in range(len(input)):
            b = set(find_basin(x, y))
            if len(b) > 1:
                basin_sizes.append(len(b))

    basin_sizes = sorted(basin_sizes, reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


input = read_input()
print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
