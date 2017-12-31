#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/3
#

import math


def find_distance(num):

    data = {}

    # create spiral

    # initial values
    data[(0, 0)] = 1
    n = 1
    x = 1
    y = 0
    d = "R"

    while True:

        n += 1
        data[(x, y)] = n

        if n == num:
            break

        if d == "R":
            # go up if possible
            if (x, y + 1) in data:
                x += 1
            else:
                y += 1
                d = "U"

        elif d == "U":
            # go left if possible
            if (x - 1, y) in data:
                y += 1
            else:
                x -= 1
                d = "L"

        elif d == "L":
            # go down if possible
            if (x, y - 1) in data:
                x -= 1
            else:
                y -= 1
                d = "D"

        elif d == "D":
            # go right if possible
            if (x + 1, y) in data:
                y -= 1
            else:
                x += 1
                d = "R"

    return abs(x) + abs(y)

assert find_distance(12) == 3
assert find_distance(23) == 2
assert find_distance(1024) == 31

print find_distance(289326)
