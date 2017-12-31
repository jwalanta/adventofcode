#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/3
#

import math


def find_sum(data, x, y):
    sum = 0
    for xx in xrange(-1, 2):
        for yy in xrange(-1, 2):
            if (x + xx, y + yy) in data:
                sum += data[(x + xx, y + yy)]

    return sum


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
        data[(x, y)] = find_sum(data, x, y)
        # print x, y, data[(x,y)]

        if data[(x, y)] > num:
            return data[(x, y)]

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


print find_distance(289326)
