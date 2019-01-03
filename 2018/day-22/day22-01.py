#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/22
#

# input
depth = 4080
targetx = 14
targety = 785

# # test input
# depth = 510
# targetx = 10
# targety = 10

gi = {}  # geological index

# compute geological indices
for x in range(0, targetx + 1):
    for y in range(0, targety + 1):
        if x == 0 and y == 0:
            gi[(x, y)] = 0
        elif x == targetx and y == targety:
            gi[(x, y)] = 0
        elif x == 0 and y != 0:
            gi[(x, y)] = y * 48271
        elif x != 0 and y == 0:
            gi[(x, y)] = x * 16807
        elif x != 0 and y != 0:
            e1 = (gi[(x - 1, y)] + depth) % 20183
            e2 = (gi[(x, y - 1)] + depth) % 20183
            gi[(x, y)] = e1 * e2

# print risk level
print sum([((gi[(x, y)] + depth) % 20183) % 3 for y in range(0, targety + 1)
           for x in range(0, targetx + 1)])
