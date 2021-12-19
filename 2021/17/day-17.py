#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/17
#

import re


def read_input():
    f = open("input.txt")
    line = f.readline()
    return list(map(int, re.findall("target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", line)[0]))


def print_grid(coordinates, target):
    x1, x2, y1, y2 = target
    miny = y1
    maxy = max([y for _, y in coordinates])
    minx = 0
    maxx = x2

    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx + 1):
            if (x, y) in coordinates:
                print("#", end="")
            elif x == 0 and y == 0:
                print("S", end="")
            elif x >= x1 and x <= x2 and y >= y1 and y <= y2:
                print("T", end="")
            else:
                print(".", end="")
        print()


def throw(vx, vy, target):
    x1, x2, y1, y2 = target
    x, y = 0, 0

    coordinates = []
    while True:

        x += vx
        y += vy

        coordinates.append((x, y))

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if x > x2 or y < y1:
            break

        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True, coordinates

    return False, coordinates


target = read_input()
print("Hang on, some crazy brute force happening...")

maxy = 0
count = 0
for vx in range(-500, 500):
    for vy in range(-500, 500):
        reached_target, coordinates = throw(vx, vy, target)
        if reached_target:
            count += 1
            maxy_in_coordinates = max([y for _, y in coordinates])
            if maxy_in_coordinates > maxy:
                maxy = maxy_in_coordinates

print("Part 1: %d" % maxy)
print("Part 2: %d" % count)
