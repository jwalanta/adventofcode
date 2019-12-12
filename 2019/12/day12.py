#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/12
#

# Part 2 notes:
# The state of axis are independent and are repeating.
# We can find the first time each axis repeats, then the LCM (least common
# multiple) of the values will be the step when they all repeat at the same time

import re
from math import gcd

f = open("input.txt")
#f = open("testinput1.txt")
lines = f.read().strip().split("\n")

# position and velocity for each moon
pos = [[], [], [], []]
vel = [[], [], [], []]

history = [{}, {}, {}]  # history for each axis

i = 0
for line in lines:
    x, y, z = map(int, re.findall(
        r"<x=([0-9\-]+), y=([0-9\-]+), z=([0-9\-]+)>", line)[0])
    pos[i] = [x, y, z]
    vel[i] = [0, 0, 0]
    i = i+1

repeats = [0, 0, 0]  # keeping track of the first time each axis repeats

step = 0
while True:

    # update velocity
    for i in range(3):  # x, y, z
        for n in range(4):  # four moons
            for m in range(4):  # consider each moon
                if n == m:  # ignore itself
                    continue
                if pos[n][i] < pos[m][i]:
                    vel[n][i] = vel[n][i] + 1
                elif pos[n][i] > pos[m][i]:
                    vel[n][i] = vel[n][i] - 1

    # update position
    for i in range(3):  # x, y, z
        for n in range(4):  # four moons
            pos[n][i] = pos[n][i] + vel[n][i]

    # part 2: save state
    for i in range(3):

        if repeats[i] > 0:
            continue

        # complete state data (position and velocity) for all moons for an axis
        state = (pos[0][i], pos[1][i], pos[2][i], pos[3][i],
                 vel[0][i], vel[1][i], vel[2][i], vel[3][i])

        if state in history[i]:  # found a repeat
            repeats[i] = step
        else:
            history[i][state] = step

    # part 2: stop if all axis have repeated at least once
    if repeats[0] > 0 and repeats[1] > 0 and repeats[2] > 0:
        break

    step = step + 1

    # part 1. find energy at 1000th step
    if step == 1000:
        # calculate energy
        energy = 0
        for n in range(4):  # four moons
            pot, kin = 0, 0
            for i in range(3):  # x, y, z
                pot = pot + abs(pos[n][i])
                kin = kin + abs(vel[n][i])
            energy = energy + (pot * kin)

        print("Part 1: %d" % energy)    


# part 2
# now we have the first repeat values for all axis, find lcm of those to find
# out when all of them repeat at the same time
lcm = repeats[0]
for n in repeats[1:]:
    lcm = lcm*n // gcd(lcm, n)

print("Part 2: %d" % lcm)
