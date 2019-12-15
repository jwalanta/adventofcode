#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/15
#

from collections import defaultdict
import curses
import heapq
import intcode

# Implementation Notes:
# - move towards *unexplored* space till a wall is hit
# - if there's a wall, rotate clockwise and try to move again
# - if there's no unexplored space around, move towards movable space which has
#   been less travelled


class Maze:

    def __init__(self, input_file, animate=True):

        self.oxygenx, self.oxygeny = None, None
        self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.grid = defaultdict(int)

        self.animate = animate

        opcode = list(map(int, open(input_file).read().strip().split(",")))
        self.droid = intcode.execute(opcode[:])

    def animate_init(self):
        if self.animate:
            self.screen = curses.initscr()
            curses.curs_set(0)  # dont display cursor

    def animate_cleanup(self):
        if self.animate:
            curses.napms(500)
            curses.endwin()

    def display_grid(self, x, y, next_dir, status):

        if not self.animate:
            return

        self.screen.addstr(x+25, y+25, ".")

        dx, dy = self.direction[next_dir]
        x, y = x+dx, y+dy

        draw = ["█", "╬", "⦿"]

        self.screen.addstr(x+25, y+25, draw[status])

        if self.oxygenx is not None:
            self.screen.addstr(self.oxygenx+25, self.oxygeny+25, draw[2])

        self.screen.refresh()
        curses.napms(5)

    # check if (x,y) in the grid is a "plus" wall. droid will never reach there
    #             #
    # like this: # #
    #             #
    def is_plus(self, x, y):
        wall_count = 0
        for dx, dy in self.direction:
            xx, yy = x+dx, y+dy
            if (xx, yy) in self.grid and self.grid[(xx, yy)] == -1:
                wall_count = wall_count + 1

        return wall_count == 4

    # is discovery done?
    # it's done if every space is visited/detected at least once
    def is_done(self):
        if len(self.grid) < 100:
            return False

        xx = [x[0] for x in self.grid.keys()]
        yy = [x[1] for x in self.grid.keys()]

        for x in range(min(xx)+1, max(xx)-2):
            for y in range(min(yy)+1, max(yy)-2):
                if (x, y) not in self.grid:
                    if self.is_plus(x, y):
                        continue
                    else:
                        return False

        return True

    # returns shortest distances from (x,y) to all possible cells
    def shortest_distances(self, x, y):

        visited = {}
        hq = [(0, x, y)]

        while hq:

            d, x, y = heapq.heappop(hq)
            if (x, y) in visited and visited[(x, y)] <= d:
                continue

            visited[(x, y)] = d

            for dx, dy in self.direction:
                xx, yy = x+dx, y+dy
                if self.grid[(xx, yy)] > 0 or self.grid[(xx, yy)] == -2:
                    heapq.heappush(hq, (d + 1, xx, yy))

        return visited

    def discover(self):

        x, y, d = 0, 0, 0

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # north (1), south (2), west (3), and east (4)
        translate = {(0, 1): 1, (1, 0): 4, (0, -1): 2, (-1, 0): 3}

        next_dir = 0

        while True:

            next(self.droid)  # run till input is needed

            # send command, get status
            status = self.droid.send(translate[direction[next_dir]])

            dx, dy = self.direction[next_dir]

            self.display_grid(x, y, next_dir, status)

            if status == 0:

                # hit a wall, change direction
                self.grid[(x+dx, y+dy)] = -1

                # turn right and check if it's open ahead
                found = False
                for _ in range(4):
                    next_dir = (next_dir + 1) % 4
                    _dx, _dy = direction[next_dir]
                    _x, _y = x+_dx, y+_dy
                    if (_x, _y) not in self.grid:
                        found = True
                        break

                # if stuck, look around and go to the path least travelled
                if not found:  # stuck
                    possibilities = []

                    for _ in range(4):
                        next_dir = (next_dir + 1) % 4
                        _dx, _dy = direction[next_dir]
                        _x, _y = x+_dx, y+_dy
                        if self.grid[(_x, _y)] > 0:
                            possibilities.append(
                                (next_dir, self.grid[(_x, _y)]))

                    assert len(possibilities) > 0

                    possibilities.sort(key=lambda x: x[1])
                    next_dir = possibilities[0][0]

            elif status == 1 or status == 2:

                # movable
                x = x + dx
                y = y + dy
                self.grid[(x, y)] = self.grid[(x, y)] + 1

                # if already been before, try going to new places
                if self.grid[(x, y)] > 1:
                    possibilities = []

                    for _ in range(4):
                        next_dir = (next_dir + 1) % 4
                        _dx, _dy = direction[next_dir]
                        _x, _y = x+_dx, y+_dy
                        if (_x, _y) in self.grid:
                            if self.grid[(_x, _y)] > 0:
                                possibilities.append(
                                    (next_dir, self.grid[(_x, _y)]))
                        else:
                            possibilities.append((next_dir, 0))

                    possibilities.sort(key=lambda x: x[1])
                    next_dir = possibilities[0][0]

            if status == 2:
                self.oxygenx, self.oxygeny = x, y

            if self.is_done():
                break

    def part1(self):
        distances = self.shortest_distances(0, 0)
        return distances[(self.oxygenx, self.oxygeny)]

    def part2(self):
        distances = self.shortest_distances(self.oxygenx, self.oxygeny)
        return max(distances.values())


maze = Maze(input_file="input.txt", animate=True)
maze.animate_init()

maze.discover()

part1 = maze.part1()
part2 = maze.part2()

maze.animate_cleanup()

print("Part 1: %d" % part1)
print("Part 2: %d" % part2)
