#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/11
#


# Using cube coordinates: https://www.redblobgames.com/grids/hexagons/
mdelta = {}
mdelta["n"] = (0, 1, -1)
mdelta["ne"] = (1, 0, -1)
mdelta["se"] = (1, -1, 0)
mdelta["s"] = (0, -1, 1)
mdelta["sw"] = (-1, 0, 1)
mdelta["nw"] = (-1, 1, 0)


def distance_from_origin(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2


def hex_grid_move(steps):

    x, y, z = 0, 0, 0

    for step in steps.split(","):

        dx, dy, dz = mdelta[step.strip()]

        x += dx
        y += dy
        z += dz

    # distance
    return distance_from_origin(x, y, z)

assert hex_grid_move("ne,ne,ne") == 3
assert hex_grid_move("ne,ne,sw,sw") == 0
assert hex_grid_move("ne,ne,s,s") == 2
assert hex_grid_move("se,sw,se,sw,sw") == 3

f = open("day11-input.txt")
print hex_grid_move(f.read())
