#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/14
#


def find_hash(str):

    input = map(ord, str) + [17, 31, 73, 47, 23]
    list = range(256)

    # - Reverse the order of that length of elements in the list,
    #   starting with the element at the current position.
    # - Move the current position forward by that length plus the skip size.
    # - Increase the skip size by one.

    skip = 0
    current = 0
    length = len(list)

    for x in range(64):  # run this 64 times
        for i in input:
            reverse = []
            for j in range(current, current + i):
                reverse = [list[j % length]] + reverse
            for j in range(i):
                list[(current + j) % length] = reverse[j]

            current += i + skip
            current %= length
            skip += 1

            # print list, current, skip

    # generate hash
    hash = [reduce(lambda i, j: i ^ j, list[i:i + 16])
            for i in range(0, 256, 16)]

    # print hash
    return ''.join(map(lambda s: format(s, '02x'), hash))


grid = {}

#testinput = "flqrgnkx"
input = "ugkiagan"

for i in range(128):
    hash = find_hash(input + "-" + str(i))
    grid[i] = ""
    for s in hash:
        grid[i] += "{0:04b}".format(int(s, 16))

    # print grid[i]


mark = {}
region = 0


def mark_region(r, c):
    if r < 0 or c < 0 or r > 127 or c > 127:
        return
    if (r, c) in mark:
        return
    if grid[r][c] == "1":
        mark[(r, c)] = 1
        mark_region(r - 1, c)
        mark_region(r + 1, c)
        mark_region(r, c + 1)
        mark_region(r, c - 1)

for r in range(128):
    for c in range(128):
        if grid[r][c] == "1" and (r, c) not in mark:
            region += 1
            # print region, r, c
            mark_region(r, c)


print region
