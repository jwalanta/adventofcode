#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2021/day/22
#

import re
from collections import defaultdict

def read_input():
    f = open("input.txt")
    lines = []
    for line in f.readlines():
        state, x1, x2, y1, y2, z1, z2 = re.findall("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", line)[0]
        lines.append([state, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)])
    return lines

def _range(a,b):
    x, y = min(a,b), max(a,b)
    x = -50 if x < -50 else x
    y = 50 if y > 50 else y
    return range(x, y+1)

steps = read_input()

onoff = defaultdict(bool)
for step in steps:
    state, x1, x2, y1, y2, z1, z2 = step
    for x in _range(x1, x2):
        for y in _range(y1, y2):
            for z in _range(z1, z2):
                onoff[(x,y,z)] = True if state == "on" else False

total_on = len([1 for _, v in onoff.items() if v])
print(total_on)


#def overlap()
    
    
