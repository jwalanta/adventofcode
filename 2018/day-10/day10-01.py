#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/10
#

# Note:
# This one won't print the answer that you can copy and paste.
# It will print the matrix that shows the phrase. It takes a while for the
# "pixels" to converge, and they start diverging again. So once you see
# something on the screen and the program stops outputting, break the program.
# Then scroll up to see the phrase.

import re

f = open("day10-input.txt")
lines = f.read().split("\n")

coord = []
for line in lines:
    x, y, dx, dy = map(
        int,
        re.findall("position=<(.*),(.*)> velocity=<(.*),(.*)>", line)[0])
    coord.append((x, y, dx, dy))

c = 0

while True:
    minx = min([x for x, y, dx, dy in coord])
    miny = min([y for x, y, dx, dy in coord])
    maxx = max([x for x, y, dx, dy in coord])
    maxy = max([y for x, y, dx, dy in coord])

    # only print if the range if less than 50 "pixels"
    if maxx - minx < 50 or maxy - miny < 50:

        print "Iteration =", c

        # create dictionary of points
        points = {(x, y): 1 for x, y, _, _ in coord}

        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x, y) in points:
                    print "#",
                else:
                    print " ",
            print

        print

    # move pixels
    for i in range(len(coord)):
        x, y, dx, dy = coord[i]
        coord[i] = (x + dx, y + dy, dx, dy)

    c = c + 1
