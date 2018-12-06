#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/6
#

f = open("day06-input.txt")
lines = f.read().split("\n")

# convert lines to tuple
coord = [tuple(map(int, i.split(","))) for i in lines]

# area map
# format: (x,y) = closest coordinate index
area = {}

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


# compute closest for each
for x in range(minx, maxx):
    for y in range(miny, maxy):
        distances = {}
        for i in range(len(coord)):
            distances[i] = mdist(x,y, coord[i][0], coord[i][1])

        # sort keys by distance
        sorted_distance = sorted(distances, key = lambda k : distances[k])

        # ignore if there are two equal minimum distances
        if distances[sorted_distance[0]] != distances[sorted_distance[1]]:
            area[(x,y)] = sorted_distance[0]

# collect the values on the edge
# these go to infinity so we can ignore them
ignore = set([])
for x in range(minx, maxx):
    for y in range(minx, maxx):
        if (x,y) in area and (x==minx or x==maxx-1 or y==miny or y==maxy-1):
            ignore.add(area[(x,y)])


# count the contained area
count = [0 for i in range(len(coord))]
for x in range(minx, maxx):
    for y in range(miny, maxy):
        if (x,y) in area and area[(x,y)] not in ignore:
            count[area[(x,y)]] = count[area[(x,y)]] + 1

# print the last item in the sorted list (largest)
print sorted(count)[-1]
