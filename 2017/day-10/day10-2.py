#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/10
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

assert find_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert find_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert find_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert find_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

print find_hash("129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108")
