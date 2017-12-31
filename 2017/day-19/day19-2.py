#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/19
#

f = open("day19-input.txt")
grid = f.read().split("\n")

# row and column
r = 0
c = grid[0].index("|")

# increments
dr = 1
dc = 0

letters = ""
count = 1  # count initial "|"

while True:

    r += dr
    c += dc

    # break loop if we're off grid or there's nothing
    if grid[r][c] == " " or r < 0 or c < 0 or r > len(grid) or c > len(grid[0]):
        break

    count += 1

    if grid[r][c].isalpha():
        letters += grid[r][c]
    elif grid[r][c] == "+":
        for tr, tc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # skip if previous r,c
            if r + tr == r - dr and c + tc == c - dc:
                continue

            if grid[r + tr][c + tc] != " ":
                dr = tr
                dc = tc
                break

print letters
print count
