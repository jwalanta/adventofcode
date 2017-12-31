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


def count_ones(str):
    count = 0
    for s in str:
        binary = "{0:04b}".format(int(s, 16))
        # print binary,
        count += binary.count("1")
    # print

    return count


#testinput = "flqrgnkx"
input = "ugkiagan"

sum = 0
for i in range(128):
    hash = find_hash(input + "-" + str(i))
    sum += count_ones(hash)

print sum
