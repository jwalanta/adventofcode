#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/3
#

f = open("input.txt")

deltas = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}

# paths[wire_number] = [(r,c), (r,c), ...] # (index = distance)
paths = [[], []]
intersections = []
visited = {}

wire = 0
for line in f.readlines():
    r, c = 0, 0
    paths[wire] = [(r, c)]

    for instr in line.split(","):
        direction, n = instr[0], int(instr[1:])
        dr, dc = deltas[direction]

        # walk through the path
        for i in range(n):
            r, c = r+dr, c+dc

            # breadcrumbs
            paths[wire].append((r, c))

            # for first wire, just store the visited locations
            if wire == 0:
                visited[(r, c)] = True

            # for second wire, check for intersections with first wire
            if wire == 1:
                if r == 0 and c == 0:   # origin doesn't count
                    continue
                if (r, c) in visited:
                    intersections.append((r, c))

    wire = wire + 1


print("Part 1: %d" % min([abs(x)+abs(y) for x, y in intersections]))

print("Part 2: %d" %
      min([paths[0].index(intersection) + paths[1].index(intersection)
           for intersection in intersections]))
