#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/10
#


def first_two_product(input, size):

    list = range(size)

    # - Reverse the order of that length of elements in the list,
    #   starting with the element at the current position.
    # - Move the current position forward by that length plus the skip size.
    # - Increase the skip size by one.

    skip = 0
    current = 0
    length = len(list)
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

    return list[0] * list[1]

assert first_two_product(map(int, "3,4,1,5".split(",")), 5) == 12

input = map(
    int, "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108".split(","))

print "Product of first two =", first_two_product(input, 256)
