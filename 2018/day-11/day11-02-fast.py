#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/11
#
# Uses summed-area table
#

serial = 3999


def power(x, y):
    p = (x + 10) * y + serial
    p = p * (x + 10)
    p = (int(p / 100) % 10) - 5

    return p


sat = [[0 for x in range(301)] for y in range(301)]

# compute summed-area table
for x in range(1, 301):
    for y in range(1, 301):
        sat[x][y] = power(
            x, y) + sat[x - 1][y] + sat[x][y - 1] - sat[x - 1][y - 1]


def power_grid(x, y, grid_size):
    return sat[x - 1][y - 1] + sat[x + grid_size - 1][y + grid_size - 1] - sat[
        x + grid_size - 1][y - 1] - sat[x - 1][y + grid_size - 1]


maxtotal = None
maxx = 0
maxy = 0
maxsize = 0

for grid_size in range(1, 301):
    print "Computing for grid size", grid_size
    for x in range(1, 301 - grid_size):
        for y in range(1, 301 - grid_size):
            total = power_grid(x, y, grid_size)
            if maxtotal == None or total > maxtotal:
                maxtotal = total
                maxx = x
                maxy = y
                size = grid_size

print "%d,%d,%d" % (maxx, maxy, size)