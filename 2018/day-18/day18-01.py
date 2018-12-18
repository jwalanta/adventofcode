#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/18
#

f = open("day18-input.txt")
lines = f.read().split("\n")

plot = {}
changed = {}

width = len(lines[0])
height = len(lines)

for r in range(height):
    for c in range(width):
        plot[(r, c)] = lines[r][c]
        changed[(r, c)] = lines[r][c]


def print_map():
    for r in range(height):
        for c in range(width):
            print plot[(r, c)],
        print

    print


def count_adjacent(rr, cc):

    count = {".": 0, "|": 0, "#": 0}

    for r in range(rr - 1, rr + 2):
        for c in range(cc - 1, cc + 2):
            if r == rr and c == cc:
                continue
            if r < 0 or c < 0 or r >= height or c >= width:
                continue
            count[plot[(r, c)]] += 1

    return count


for i in range(10):

    for r in range(height):
        for c in range(width):

            x = plot[(r, c)]
            n = count_adjacent(r, c)

            if x == ".":
                if n["|"] >= 3:
                    changed[(r, c)] = "|"
                else:
                    changed[(r, c)] = "."
            elif x == "|":
                if n["#"] >= 3:
                    changed[(r, c)] = "#"
                else:
                    changed[(r, c)] = "|"
            elif x == "#":
                if n["#"] >= 1 and n["|"] >= 1:
                    changed[(r, c)] = "#"
                else:
                    changed[(r, c)] = "."

    # copy back
    for r in range(height):
        for c in range(width):
            plot[(r, c)] = changed[(r, c)]

wood = sum([1 for p in plot.itervalues() if p == "|"])
lumber = sum([1 for p in plot.itervalues() if p == "#"])

print wood * lumber
