#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/11
#

from collections import defaultdict

input = 3999


def power(x, y, serial):
    p = (x + 10) * y + serial
    p = p * (x + 10)
    n = int(p / 100) % 10
    p = n - 5

    return p


# compute total power for 3x3 grid at (x,y)
def power_33grid(x, y, serial):
    total = 0
    for xx in range(x, x + 3):
        for yy in range(y, y + 3):
            total = total + power(xx, yy, serial)

    return total


max = 0
maxx = 0
maxy = 0
for x in range(1, 298):
    for y in range(1, 298):
        total = power_33grid(x, y, input)
        if total > max:
            max = total
            maxx = x
            maxy = y

print "%d,%d" % (maxx, maxy)
