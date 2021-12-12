#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/12
#

from collections import defaultdict

cave = defaultdict(list)


def read_input():
    f = open("input.txt")
    for l in f.readlines():
        s, e = l.strip().split("-")
        cave[s].append(e)
        cave[e].append(s)


def find_paths(path, small_cave_exhausted):
    for next in cave[path[-1]]:
        if next == "start":
            continue

        if next == "end":
            paths.append(path + [next])
        elif next[0].isupper() or path.count(next) == 0:
            find_paths(path + [next], small_cave_exhausted)
        elif path.count(next) == 1 and small_cave_exhausted == False:
            find_paths(path + [next], True)


read_input()

paths = []
find_paths(['start'], True)
print("Part 1: %d" % len(paths))

paths = []
find_paths(['start'], False)
print("Part 2: %d" % len(paths))
