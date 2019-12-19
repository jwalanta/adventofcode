#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/19
#

import intcode

opcode = list(map(int, open("input.txt").read().strip().split(",")))

# check if (x,y) is inside the beam
def inside_beam(x, y):
    drone = intcode.execute(opcode[:])
    next(drone)  # run till next input
    drone.send(x)  # send x
    n = drone.send(y)  # send y, next output will be beam/no-beam
    return n == 1


def part1():
    return sum([1 if inside_beam(x, y) else 0 for x in range(50) for y in range(50)])



# follow the bottom beam line and check if the upper right coordinate is inside
# the beam
def part2():

    x, y = 0, 100 # first few lines are weird and dont contain beam signals
                  # so start with y=100
    drone_size = 100

    while True:
        while not inside_beam(x, y):
            x += 1

        if inside_beam(x+drone_size-1, y-drone_size+1): # upper right
            return x*10000 + (y-drone_size+1) # upper left

        y += 1


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
