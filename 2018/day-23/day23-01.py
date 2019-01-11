#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/23
#

import re

f = open("day23-input.txt")
lines = f.read().split("\n")

bots = []

maxbot = None
for line in lines:
    x,y,z,r = map(int, re.findall("pos=<(.*),(.*),(.*)>, r=(.*)", line)[0])
    bots.append((x,y,z,r))
    if maxbot == None or r > maxbot[3]:
        maxbot = (x,y,z,r)

print maxbot

count = 0
for b in bots:
    x1, y1, z1, r1 = maxbot
    x2, y2, z2, r2 = b

    d = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

    if d <= r1:
        count += 1

print count