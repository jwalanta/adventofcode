#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2019/day/10
#

import math

grid = open("input.txt").read().strip().split("\n")
#grid = open("testinput1.txt").read().strip().split("\n")
#grid = open("testinput5.txt").read().strip().split("\n")

asteroids = [(y, x) for x in range(len(grid))
             for y in range(len(grid[0])) if grid[x][y] == "#"]
# ^ (y,x) because of the coordinate system

#
# Part 1
#
max_count = 0
max_x = 0
max_y = 0
max_angles = None
for x1, y1 in asteroids:

    # find the angles between asteroid at (x1,y1) and the rest of the asteroids
    #
    # for a given asteroid a1, if the angle between a1 and a2 is the same as a1
    # and a3, then only one (a2 or a3) of them is in direct line of sight from a1
    angles = {}
    for x2, y2 in asteroids:
        if x1 == x2 and y1 == y2:  # itself
            continue

        # TIL: atan2. got the idea from reddit
        angles[(x2, y2)] = math.atan2(y2-y1, x2-x1)

    # total non repeated angles (set) == total visible asteroids for (x1, y1)
    if len(set(angles.values())) > max_count:
        max_count = len(set(angles.values()))
        max_x = x1
        max_y = y1
        max_angles = angles.copy()


print("Part 1: %d" % max_count)


#
# Part 2
#

# create a list of coordinates, angles, and distance so that we can sort them
targets = []
for (x, y), angle in max_angles.items():
    angle = math.degrees(angle)

    # lasers start pointed upwards, so adjust the angle values
    angle = angle + 90

    # change all negative degrees to 0-360 scale
    angle = angle + (360 if angle < 0 else 0)

    # distance
    dist = (x-max_x) ** 2 + (y-max_y) ** 2

    targets.append((x, y, angle, dist))


# sort by angle, then by distance
# angle, because laser moves clockwise
# distance, because for same angle, nearest one is destroyed first
targets.sort(key=lambda x: (x[2], x[3]))

# pew pew pew
i = 0
count = 0
destroyed = []
prev_angle = None
while len(destroyed) < len(targets):

    x, y, angle, dist = targets[i]

    if i in destroyed:  # already destroyed, ignore
        continue

    # ignore any consecutive asteriods with same line of sight angle,
    # otherwise destroy
    if prev_angle == None or prev_angle != angle:
        destroyed.append(i) # pew pew
        count = count + 1

    prev_angle = angle

    if count == 200:
        print("Part 2: %d" % (x*100+y))
        break

    i = (i+1) % len(targets)
