#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/21
#


def get_variations(pattern):
    variations = []
    p = map(list, pattern.split("/"))

    for i in range(4):
        # rotate
        p = zip(*p[::-1])
        variations.append("/".join(map(lambda x: "".join(x), p)))

        # add flipped variation
        variations.append("/".join(map(lambda x: "".join(x), p[::-1])))

    return variations


# read enhancement rules
f = open("day21-input.txt")

# input
enhancements = {}
for line in f:
    p = line.split(" => ")
    enhancements[p[0]] = p[1].strip()

    # get all variations of the pattern and add them too
    for v in get_variations(p[0]):
        enhancements[v] = p[1].strip()

# initial grid
grid = map(list, ".#./..#/###".split("/"))

# iterate for n times
for x in range(5):
    if len(grid) % 2 == 0:
        size = 2
    elif len(grid) % 3 == 0:
        size = 3

    final_size = (len(grid) / size) * (size + 1)

    grid_temp = [['' for i in range(final_size)] for j in range(final_size)]

    for i in range(0, len(grid), size):
        for j in range(0, len(grid), size):

            # get sub matrix string
            pattern = ""
            for ii in range(i, i + size):
                for jj in range(j, j + size):
                    pattern += grid[ii][jj]
                pattern += "/"
            pattern = pattern[0:-1]

            # get enhancement
            enhancement = enhancements[pattern]

            # put it back in grid_temp
            m = map(list, enhancement.split("/"))

            for ii in range(len(m)):
                for jj in range(len(m)):
                    ei = (i / size) * (size + 1) + ii
                    ej = (j / size) * (size + 1) + jj
                    grid_temp[ei][ej] = m[ii][jj]

    grid = grid_temp


# print and get count
count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        print grid[i][j],
        if grid[i][j] == "#":
            count += 1
    print

print count
