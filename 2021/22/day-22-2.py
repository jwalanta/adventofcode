#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/22
#

import re
from collections import defaultdict

def read_input():
    f = open("test.txt")
    lines = []
    for line in f.readlines():
        state, x1, x2, y1, y2, z1, z2 = re.findall("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", line)[0]
        lines.append([state, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)])
    return lines

# |         |
# |         |
# a1--------a2
#     +     +  <- intersection points
#     b1----------b2
#     |           |
#     |           |
def overlap(a1, a2, b1, b2):
    if a2 < b1 or b2 < a1:
        return 0
    
    _, a,b, _ = sorted([a1, a2, b1, b2])
    return abs(a-b) + 1


def total_intersection_cubes(step1, step2):
    _, ax1, ax2, ay1, ay2, az1, az2 = step1
    _, bx1, bx2, by1, by2, bz1, bz2 = step2

    x = overlap(ax1, ax2, bx1, bx2)
    y = overlap(ay1, ay2, by1, by2)
    z = overlap(az1, az2, bz1, bz2)

    return x*y*z


def total_cubes(step):
    _, x1, x2, y1, y2, z1, z2 = step
    return (abs(x1-x2)+1) * (abs(y1-y2)+1) * (abs(z1-z2)+1)

steps = read_input()

total = 0

# first count all on cubes
for i in range(len(steps)):
    state, x1, x2, y1, y2, z1, z2 = steps[i]
    print(state, x1, x2, y1, y2, z1, z2)
    if state == "off":
        continue
    total += total_cubes(steps[i])


# remove intersections
intersections = []
for i in range(len(steps)):
    for j in range(len(steps)):
        if i == j or steps[i][0] == "off" or steps[j][0] == "off":
            continue

        if (i,j) in intersections:
            continue

        intersections.append((i,j))
        intersections.append((j,i))

        total -= total_intersection_cubes(steps[i], steps[j])

# remove offs
# for i in range(len(steps)):
#     state, x1, x2, y1, y2, z1, z2 = steps[i]
#     if state == "on":
#         continue
#     total -= total_cubes(steps[i])

print(total)




