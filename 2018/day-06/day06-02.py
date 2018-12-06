#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/6
#

f = open("day06-input.txt")
lines = f.read().split("\n")

# convert lines to tuple
coord = [tuple(map(int, i.split(","))) for i in lines]

# manhattan distance
def mdist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# compute range
# (minx, miny) to (maxx, maxy) expanded by 
# width and height to provide enough space
minx = min([p[0] for p in coord])
maxx = max([p[0] for p in coord])
miny = min([p[1] for p in coord])
maxy = max([p[1] for p in coord])
dx = maxx-minx
dy = maxy-miny

# expand
minx = minx - dx
maxx = maxx + dx
miny = miny - dy
maxy = maxy + dy

# compute closest for each coordinate in the map
max = 10000
total_size = 0
for x in range(minx, maxx):
    for y in range(miny, maxy):
        total = 0
        for i in range(len(coord)):
            total = total + mdist(x,y, coord[i][0], coord[i][1])

        if total < max:
            total_size = total_size + 1

print total_size
            




