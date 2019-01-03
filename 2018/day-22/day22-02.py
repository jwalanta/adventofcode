#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/22
#

import heapq

# input
depth = 4080
targetx = 14
targety = 785

# # test input
# depth = 510
# targetx = 10
# targety = 10

gi = {}  # geological index


def erosion(x, y):
    if (x, y) in gi:
        pass
    elif x == 0 and y == 0:
        gi[(x, y)] = 0
    elif x == targetx and y == targety:
        gi[(x, y)] = 0
    elif x == 0 and y != 0:
        gi[(x, y)] = y * 48271
    elif x != 0 and y == 0:
        gi[(x, y)] = x * 16807
    elif x != 0 and y != 0:
        gi[(x, y)] = erosion(x - 1, y) * erosion(x, y - 1)

    return (gi[(x, y)] + depth) % 20183


def region_type(x, y):
    return erosion(x, y) % 3


# pre-compute GI till (targetx, targety)
for y in range(0, targety + 1):
    for x in range(0, targetx + 1):
        region_type(x, y)

# predefined values
rocky, wet, narrow = 0, 1, 2
neither, torch, climbing_gear = 0, 1, 2

# which equipment is valid for the region?
valid_equipments = {
    rocky: [torch, climbing_gear],
    wet: [neither, climbing_gear],
    narrow: [neither, torch]
}

# delta for neighbors
neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# heap queue (time, x,y, equipment)
hq = [(0, 0, 0, torch)]  # start with torch at (0,0)

# visited list
visited = {}

while hq:
    time, x, y, equipment = heapq.heappop(hq)

    if (x, y, equipment) in visited and visited[(x, y, equipment)] <= time:
        continue

    visited[(x, y, equipment)] = time

    if (x, y, equipment) == (targetx, targety, torch):
        print time
        break

    current_region_type = region_type(x, y)
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy

        # ignore out of bounds
        if nx < 0 or ny < 0:
            continue

        target_region_type = region_type(nx, ny)

        # check if we can go to new region without equipment change
        if equipment in valid_equipments[target_region_type]:
            heapq.heappush(hq, (time + 1, nx, ny, equipment))

        # see which equipment we can change to and go to the region
        for eq in range(3):
            if eq == equipment:  # cant use same equipment
                continue

            if eq in valid_equipments[current_region_type] and eq in valid_equipments[target_region_type]:
                heapq.heappush(hq, (time + 8, nx, ny, eq))
