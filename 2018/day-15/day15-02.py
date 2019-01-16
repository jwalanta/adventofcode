#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/15
#

import os
import heapq
from time import sleep

NEIGHBORS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# raise this exception at any point simulation is invalid
# invalid = elf dies or elves dont win
class InvalidSimulation(Exception):
    def __init__(self, maze):
        self.maze = maze


# Elf or Goblin
class Unit:
    def __init__(self, r, c, type, attack_power):
        self.r = r
        self.c = c
        self.type = type
        self.attack_power = attack_power
        self.hit_points = 200

    def get_coord(self):
        return (self.r, self.c)

    def get_type(self):
        return self.type

    def attacks(self, unit):
        unit.gets_attacked(self.attack_power)

    def gets_attacked(self, attack_power):
        self.hit_points = self.hit_points - attack_power


# Maze Simulation
class Maze:
    def __init__(self, filename, elf_power):

        f = open(filename)
        lines = f.read().split("\n")

        self.barrier = {}
        self.units = []

        self.height = len(lines)
        self.width = len(lines[0])

        for r in range(self.height):
            for c in range(self.width):
                if lines[r][c] == "#":
                    self.barrier[(r, c)] = "#"
                elif lines[r][c] in "GE":
                    attack_power = elf_power if lines[r][c] == "E" else 3
                    self.units.append(Unit(r, c, lines[r][c], attack_power))

        self.elves_count = len([u for u in self.units if u.type == "E"])
        self.goblins_count = len([u for u in self.units if u.type == "G"])

    def unit_exists(self, r, c):
        for u in self.units:
            if u.get_coord() == (r, c) and u.hit_points > 0:
                return u.get_type()

        return None

    def get_unit_at(self, r, c):
        for u in self.units:
            if u.get_coord() == (r, c) and u.hit_points > 0:
                return u

        return None

    # yield valid adjacent cells for a given (r,c) location
    def neighbors(self, r, c):
        # north, west, east, south
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr >= self.width or nr >= self.height or (
                    nr, nc) in self.barrier or self.unit_exists(nr, nc):
                continue

            yield (nr, nc)

    def display(self, count=0):

        os.system("clear")
        print "After", count, "round:"

        RED = '\33[31m'
        GREEN = '\33[32m'
        ENDC = '\033[0m'

        units = {u.get_coord(): (u.type, u.hit_points) for u in self.units}

        for r in range(self.height):
            hits_str = []
            for c in range(self.width):

                if (r, c) in self.barrier:
                    print "#",
                elif (r, c) in units:
                    hits_str.append(units[(r, c)][0] + "(" +
                                    str(units[(r, c)][1]) + ")")

                    if units[(r, c)][0] == "G":
                        print GREEN + units[(r, c)][0] + ENDC,
                    else:
                        print RED + units[(r, c)][0] + ENDC,
                else:
                    print ".",
            print ", ".join(hits_str)

        print
        sleep(0.1)

    def print_count(self):
        elves = [u for u in self.units if u.type == "E" and u.hit_points > 0]
        goblins = [u for u in self.units if u.type == "G" and u.hit_points > 0]
        print "Total Elves = ", len(elves), [u.hit_points for u in elves]
        print "Total Goblins = ", len(goblins), [u.hit_points for u in goblins]
        print

    # returns shortest distances from (r,c) to all possible cells
    def shortest_distances(self, r, c):

        visited = {}
        hq = [(0, r, c)]

        while hq:

            d, r, c = heapq.heappop(hq)
            if (r, c) in visited and visited[(r, c)] <= d:
                continue

            visited[(r, c)] = d

            for nr, nc in self.neighbors(r, c):
                heapq.heappush(hq, (d + 1, nr, nc))

        return visited

    # traces shortest path (considering tie breakers), given shortest distances
    def shortest_path(self, distances, r, c, tr, tc):
        path = [(tr, tc)]

        while True:
            cr, cc = path[-1]
            possible = []
            for dr, dc in NEIGHBORS:
                nr, nc = cr + dr, cc + dc

                # start found?
                if (nr, nc) == (r, c):
                    return path[::-1]

                if (nr, nc) in distances:
                    possible.append((distances[(nr, nc)], nr, nc))

            assert len(possible) > 0

            # out of possible moves, pick the shortest. ties are broken top to
            # bottom, left to right (by virtue of tuple being (distance, r, c))
            possible = sorted(possible)
            path.append((possible[0][1], possible[0][2]))

    # run the simulation
    def run(self):

        count = 0  # round count

        while True:

            # sort units by position
            self.units = sorted(self.units, key=lambda u: (u.r, u.c))

            for unit in self.units:

                # skip if the unit has died during this round
                if unit.hit_points <= 0:
                    continue

                #
                # try to move
                #

                # check if adjacent cell is the target
                adjacent_in_range = []
                for dr, dc in NEIGHBORS:
                    nr, nc = unit.r + dr, unit.c + dc
                    u = self.get_unit_at(nr, nc)

                    if u != None and u.type != unit.type and u.hit_points > 0:
                        adjacent_in_range.append((u.hit_points, nr, nc))

                # move if there are not targets in adjacent cells
                if len(adjacent_in_range) == 0:

                    distances = self.shortest_distances(unit.r, unit.c)

                    # find possible targets
                    target_units = [
                        u for u in self.units
                        if u.type != unit.type and u.hit_points > 0
                    ]

                    # find targets that are reachable
                    target_distances = []
                    for tu in target_units:
                        for nr, nc in self.neighbors(tu.r, tu.c):
                            if (nr, nc) in distances:
                                target_distances.append((distances[(nr, nc)],
                                                         nr, nc))

                    if len(target_distances) > 0:

                        # sort by distance, then by row and column
                        # the first item is the closest
                        # ties are already broken by row and column while sorting
                        target_distances = sorted(target_distances)

                        tr, tc = target_distances[0][1], target_distances[0][2]

                        # find shortest path
                        shortest_path = self.shortest_path(
                            distances, unit.r, unit.c, tr, tc)

                        # step forward
                        unit.r, unit.c = shortest_path[0]

                #
                # try to attack
                #

                # re-check if adjacent cell is the target
                # this has to be recomputed because units have possibly moved
                adjacent_in_range = []
                for dr, dc in NEIGHBORS:
                    nr, nc = unit.r + dr, unit.c + dc
                    u = self.get_unit_at(nr, nc)

                    if u != None and u.type != unit.type and u.hit_points > 0:
                        adjacent_in_range.append((u.hit_points, nr, nc))

                # attack if there are no targets
                if len(adjacent_in_range) > 0:

                    # attack the weakest, ties broken by row & col
                    adjacent_in_range = sorted(adjacent_in_range)
                    u = self.get_unit_at(adjacent_in_range[0][1],
                                         adjacent_in_range[0][2])
                    u.gets_attacked(unit.attack_power)

                    if u.type == "E" and u.hit_points <= 0:
                        raise InvalidSimulation(self)

            # remove dead units
            self.units = [u for u in self.units if u.hit_points > 0]

            # quit if there are no targets
            numg = len([u for u in self.units if u.type == "G"])
            nume = len([u for u in self.units if u.type == "E"])

            if nume == 0 or nume != self.elves_count:
                raise InvalidSimulation(self)

            if numg == 0:
                break

            count += 1
            #self.display(count)

        #self.display(count)
        self.print_count()
        print "-" * 30
        print "Total rounds =", count
        print "Outcome =", count * sum([u.hit_points for u in self.units])


elf_power = 4
while True:
    try:
        print "Elf Power = ", elf_power
        maze = Maze("day15-input.txt", elf_power)
        maze.run()
        print "Valid :)"
        break
    except InvalidSimulation as err:
        print "Invalid :("
        err.maze.print_count()
        elf_power += 1
