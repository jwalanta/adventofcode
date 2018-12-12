#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/11
#

from collections import defaultdict

print "TOO SLOW. EXPECT TO WAIT HOURS."

input = 3999

powers = {}


def power(x, y, serial):
    p = (x + 10) * y + serial
    p = p * (x + 10)
    n = int(p / 100) % 10
    p = n - 5

    return p


def power_grid_size(x, y, size):
    total = 0
    for xx in range(x, x + size):
        for yy in range(y, y + size):
            total = total + powers[(xx, yy)]

    return total


# precompute powers
for x in range(1, 301):
    for y in range(1, 301):
        powers[(x, y)] = power(x, y, input)

max = 0
maxx = 0
maxy = 0
size = 0

for grid_size in range(1, 301):
    print "Computing for grid size", grid_size
    for x in range(1, 301 - grid_size):
        for y in range(1, 301 - grid_size):
            total = power_grid_size(x, y, grid_size)
            if total > max:
                max = total
                maxx = x
                maxy = y
                size = grid_size

print "%d,%d,%d" % (maxx, maxy, size)
