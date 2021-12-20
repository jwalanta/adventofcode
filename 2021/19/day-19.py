#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/19
#

from collections import defaultdict


def read_input():
    f = open("input.txt")

    scanners = defaultdict(set)
    scanner = -1
    for line in f.readlines():
        if "scanner" in line:
            scanner += 1
            continue

        if line.strip() != "":
            scanners[scanner].add(tuple(map(int, line.strip().split(","))))

    return dict(scanners)


def get_rotated_beacons(n, beacons):
    new_beacons = []

    for b in beacons:
        x, y, z = b

        possible_rotations = [
            (x, y, z),
            (y, -x, z),
            (-x, -y, z),
            (-y, x, z),
            (y, z, x),
            (-x, z, y),
            (-y, z, -x),
            (x, z, -y),
            (z, x, y),
            (z, y, -x),
            (z, -x, -y),
            (z, -y, x),
            (y, x, -z),
            (-x, y, -z),
            (-y, -x, -z),
            (x, -y, -z),
            (x, -z, y),
            (y, -z, -x),
            (-x, -z, -y),
            (-y, -z, x),
            (-z, y, x),
            (-z, -x, y),
            (-z, -y, -x),
            (-z, x, -y)
        ]

        new_beacons.append(possible_rotations[n])

    return new_beacons


def get_delta(b1, b2):
    x1, y1, z1 = b1
    x2, y2, z2 = b2
    return (x1-x2, y1-y2, z1-z2)


def get_moved_beacons(beacons, delta):
    dx, dy, dz = delta
    new_beacons = []
    for b in beacons:
        x, y, z = b
        new_beacons.append((x+dx, y+dy, z+dz))

    return set(new_beacons)

# check if there are 12 or more common beacons between scanner1 and scanner2
# transform beacons from one scanner to another for each beacon and check matches
def find_match(scanner1, scanner2):
    for b1 in scanner1:
        for b2 in scanner2:
            # print(b1, b2)
            d = get_delta(b1, b2)
            moved_beacons = get_moved_beacons(scanner2, d)

            matched_beacons = scanner1 & moved_beacons
            if len(matched_beacons) >= 12:
                return True, d, moved_beacons

    return False, None, None


def manhattan_distance(b1, b2):
    x1, y1, z1 = b1
    x2, y2, z2 = b2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)


scanners = read_input()

#
# part 1
#

resolved_beacons = scanners[0]   # use first scanner as reference
unresolved_scanners = [i for i in range(1, len(scanners))]
scanner_locations = [(0, 0, 0)]

while len(unresolved_scanners) > 0:
    beacons = scanners[unresolved_scanners[0]]
    added = False

    # rotate beacons for the scanner and see if they line up with resolved beacons
    for i in range(24):
        rotated_beacons = get_rotated_beacons(i, beacons)
        matched, delta, new_beacons = find_match(resolved_beacons, rotated_beacons)
        if matched:
            added = True
            resolved_beacons |= new_beacons
            unresolved_scanners = unresolved_scanners[1:]
            scanner_locations.append(delta)
            print("Scanners to resolve: ", len(unresolved_scanners))

    # there might not be any overlapping beacons.
    # if the scanner can't be resolved, send it back of the queue
    if added == False:
        unresolved_scanners = unresolved_scanners[1:] + unresolved_scanners[:1]


print("Part 1: %d" % len(resolved_beacons))

#
# part 2
#

# print(scanner_locations)
max_manhattan_distance = 0
for b1 in scanner_locations:
    for b2 in scanner_locations:
        d = manhattan_distance(b1, b2)
        max_manhattan_distance = d if d > max_manhattan_distance else max_manhattan_distance

print("Part 2: %d" % max_manhattan_distance)
