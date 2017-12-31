#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/22
#

nodes = {}

# directions clockwise
directions = ["U", "R", "D", "L"]
delta = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

# read initial map
input_str = open("day22-input.txt").read().strip()

m = map(list, input_str.split("\n"))
for r in range(len(m)):
    for c in range(len(m)):
        if m[r][c] == "#":
            nodes[(r, c)] = "#"

# initial conditions
r = c = len(m) / 2
d = "U"

# - If the current node is infected, it turns to its right.
#   Otherwise, it turns to its left. (Turning is done in-place;
#   the current node does not change.)
# - If the current node is clean, it becomes infected.
#   Otherwise, it becomes cleaned. (This is done after the node
#   is considered for the purposes of changing direction.)
# - The virus carrier moves forward one node in the direction it is facing.

infection = 0
for burst in range(10000):
    if (r, c) not in nodes:
        nodes[(r, c)] = ""

    if nodes[(r, c)] == "#":
        # turn right
        d = directions[(directions.index(d) + 1) % len(directions)]

    elif nodes[(r, c)] == "":
        # turn left
        d = directions[(directions.index(d) - 1) % len(directions)]

    if nodes[(r, c)] == "":
        nodes[(r, c)] = "#"
        infection += 1
    else:
        nodes[(r, c)] = ""

    # move forward
    dr, dc = delta[d]
    r += dr
    c += dc


print "Total Infection", infection
