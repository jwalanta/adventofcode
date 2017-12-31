#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2017/day/12
#

f = open("day12-input.txt")

connection = {}
for line in f:
    p1 = line.split(" <-> ")[0]
    p2 = map(lambda x: x.strip(), line.split(" <-> ")[1].split(", "))
    connection[p1] = p2


def can_reach(program):
    return [p for p in connection if program in connection[p]]


def get_group(program):

    group = set([program])
    explored = {}
    while True:
        child_group = set([])
        for p in group:
            if p in explored:
                continue
            child_group |= set(can_reach(p))
            explored[p] = 1

        if group == child_group or len(child_group) == 0:
            break
        group |= child_group

    return list(group)

print "Group size for 0:", len(get_group('0'))

unique_groups = {}
explored = set([])

# find groups for all programs
for p in connection:

    if p in explored:
        continue

    group = get_group(p)
    group.sort()

    # keep track of already visited program
    explored |= set(group)

    unique_groups[tuple(group)] = 1

print "Unique groups:", len(unique_groups)
