#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/18
#

from collections import defaultdict

f = open("day18-input.txt")
lines = f.read().split("\n")

# part 2 input
input = 1000000000

# the pattern repeats after a while, so we need to find when it starts repeating
# and what's the repitition length. we can use this value to find value for any
# number of cycles after that

plot = {}
changed = {}
solutions = {}

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


repeat_lengths = defaultdict(int)
wood_lumber = []
repeat_start = None

for i in range(600):

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
    product = wood * lumber

    # check for repetition
    if product in wood_lumber:
        # print i, wood, lumber, product, "REPEAT"
        repeat_lengths[i - wood_lumber.index(product)] += 1

        if repeat_start == None:
            repeat_start = i

    else:
        # print i, wood, lumber, product
        repeat_start = None

    wood_lumber.append(product)

# find the repeat length that happens the most
repeat_length = max(repeat_lengths, key=lambda k: repeat_lengths[k])

index = (input - 1 - repeat_start) % repeat_length
print wood_lumber[repeat_start + index]
