#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/15
#

import heapq

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_input():
    m = []
    f = open("input.txt")
    for l in f.readlines():
        m.append(list(map(int, list(l.strip()))))

    return m


def shortest_distances(x, y):
    visited = {}
    hq = [(0, x, y)]

    while hq:
        d, x, y = heapq.heappop(hq)
        if (x, y) in visited and visited[(x, y)] <= d:
            continue

        visited[(x, y)] = d

        for dx, dy in direction:
            xx, yy = x + dx, y + dy
            if xx < 0 or yy < 0 or xx >= len(grid[0]) or yy >= len(grid):
                continue
            heapq.heappush(hq, (d + grid[xx][yy], xx, yy))

    return visited


def expand_grid():
    new_grid = []

    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
    nx, ny = len(grid[0]), len(grid)

    for x in range(nx * 5):
        l = []
        for y in range(ny * 5):
            mx, rx = x // nx, x % nx
            my, ry = y // ny, y % ny

            v = grid[rx][ry]

            i = d.index(v)
            v = d[i + mx]

            i = d.index(v)
            v = d[i + my]

            l.append(v)

        new_grid.append(l)

    return new_grid


grid = read_input()

d = shortest_distances(0, 0)
print("Part 1: %d" % d[(len(grid[0]) - 1, len(grid) - 1)])

grid = expand_grid()
d = shortest_distances(0, 0)
print("Part 2: %d" % d[(len(grid[0]) - 1, len(grid) - 1)])
